########################################################################################################################

#GOAL: Create content database of trending articles for marketing

# This script extends an unofficial Google Trends API
# It adds a missing request for Real-Time data
# It creates an initial excel spreadsheet with the downloaded dataframe
# New articles are added into the existing spreadsheet when re-run
# Article data is cleaned, split up, and hashtags generated based on title

########################################################################################################################

from pytrends.request import TrendReq
import pandas as pd
import numpy as np
from pprint import pprint
import xlsxwriter
from datetime import date
import dateparser
import re
import time
########################################################################################################################
# INCREASE DEFAULT COLUMN VISIBILITY

desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 26)
pd.set_option('display.max_rows', 100)

########################################################################################################################
# FUNCTIONS

class MyTrendReq(TrendReq):
    """Request data from Google Daily Trends section and returns a dataframe"""
    REAL_TIME_TRENDS_URL = 'https://trends.google.com/trends/api/realtimetrends'
    def real_time_data(self):
        forms = {'geo': 'US', # Location
                 'tz': '300', # TimeZone
                 'hl': 'en-US', # Language
                 'cat': 'm', #Category m = health
                 'fi': '0',
                 'fs': '0',
                 'ri': '300',
                 'rs': '20',
                 'sort': '0'}
        req_json = self._get_data(
            url=MyTrendReq.REAL_TIME_TRENDS_URL,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
            params=forms)
        req_json = req_json['storySummaries']['trendingStories']
        df = pd.DataFrame.from_dict(req_json, orient='columns')
        return df

    ##################################################################################
    def update(self, df):
        trendfile = 'C:/Users/Emil/PycharmProjects/dataanalysis/Data/trenddata.xlsx'
        writer = pd.ExcelWriter(trendfile, engine='xlsxwriter')
        audit_table = pd.read_excel(trendfile)
        appended_audit = audit_table.append(df, sort=False)  # Populate file
        appended_audit.to_excel(writer, sheet_name='Audit', index=False)  # Save file
        print("Saving Updated File with New Data")

        writer.save()
        writer.close()

    ##################################################################################
    def clean(self, df):
        df = df.replace(to_replace=r'&#39;', value="'", regex=True) # Replace characters
        df = df.replace(to_replace=r'&nbsp;', value="... read more, link below!...", regex=True)  # Replace characters
        df = df.drop_duplicates(subset="URL")
        return df
    ##################################################################################
    # BUILD CORE DATAFRAME
    def build( self, df):

        df = rt[['title', 'articles', 'image']]
        dict = []
        for i, row in df.iterrows():
            for article in row.articles:
                image = row['image']
                if image.get('imgUrl', None):
                    dict.append(
                        {'Title': row.title,
                         'Source': article['source'],
                         'time': dateparser.parse(article['time']).strftime('%x %X'),
                         'timestring': article['time'],
                         'Article Title': article['articleTitle'],
                         'Snippet': article['snippet'],
                         'URL': article['url'],
                         'imageUrl': image.get('imgUrl'),
                         'timesort': dateparser.parse(article['time'])})
        df2 = pd.DataFrame.from_dict(dict, orient='columns')

        return df2

    ##################################################################################
    def compare(self, df):
        trendfile = 'C:/Users/Emil/PycharmProjects/dataanalysis/Data/trenddata.xlsx'
        old_table = pd.read_excel(trendfile)
        old_set = set(old_table["URL"])
        print("Previous File Length:", len(old_set))
        realtime_set = set(df["URL"])
        new = realtime_set-old_set
        new_titles = df[df['URL'].isin(new)]                             # NEW TITLES
        updated_table = old_table.append(new_titles, sort=False)         # Add new to old titles, false keeps col order
        ##################################################################################
        # ADD HASHTAGS
        for i, row in updated_table.iterrows():
            title = row['Title']
            hashtag = re.sub(r"([A-Za-z0-9!@#$%^&*()]+)", r"#\1", title)
            hashtag = re.sub(r",", r"", hashtag)
            updated_table.at[i, 'Hashtag'] = hashtag
        ##################################################################################
        # MERGE CONTENT
        for i, row in updated_table.iterrows():
            articleTitle = row['Article Title']
            snippet = row['Snippet']
            url = row['URL']
            hashtag = row['Hashtag']
            updated_table.at[i, 'Content'] = articleTitle + '\n\n' + snippet + '\n\n' + url + '\n\n' + hashtag

        ##################################################################################
        writer = pd.ExcelWriter(trendfile, engine='xlsxwriter')          # Initiate writer
        updated_table = updated_table.sort_values(by=['timesort'], ascending=False)
        updated_table.to_excel(writer, sheet_name='Audit', index=False)  # Save audit file
        writer.save()
        writer.close()
        print("Trend File has been updated with%3d new titles"%(len(new_titles)))
        print("Total File length is:", len(updated_table))

    ##################################################################################

########################################################################################################################
# MAIN

while True:
    pytrend = MyTrendReq()
    rt = pytrend.real_time_data()
    df = pytrend.build(rt)
    df = pytrend.clean(df)
    print("Real time count:", len(df))
    # pytrend.update(df)                                                          # Only run once to create baseline
    df = pytrend.compare(df)
    time.sleep(900) # run every 15min

########################################################################################################################


















''' NOTES FOR LATER '''
# # Download images from URL | Use this when the systems knows which article to pst (Post clasification)
# import urllib.request
# urllib.request.urlretrieve("URL", "local-filename.jpg")
