from pytrends.request import TrendReq
import pandas as pd
import numpy as np
from pprint import pprint
import xlsxwriter
from datetime import date
import dateparser
import re
##################################################################################
# INCREASE DEFAULT COLUMN VISIBILITY

desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 26)
pd.set_option('display.max_rows', 100)

##################################################################################
# FUNCTIONS

class MyTrendReq(TrendReq):
    REAL_TIME_TRENDS_URL = 'https://trends.google.com/trends/api/realtimetrends'

    def real_time_data(self, pn='US', category = 'all'):
        """Request data from Google Daily Trends section and returns a dataframe"""

        forms = {'geo': pn,
                 'tz': '300',
                 'hl': 'en-US',
                 'cat': 'm',
                 'fi': '0',
                 'fs': '0',
                 'ri': '300',
                 'rs': '20',
                 'sort': '0'}
        req_json = self._get_data(
            url=MyTrendReq.REAL_TIME_TRENDS_URL,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
            params=forms
        )

        req_json = req_json['storySummaries']['trendingStories']
        df = pd.DataFrame.from_dict(req_json, orient='columns')
        return df

    ##################################################################################
    def update(self, df):

        trendfile = 'C:/Users/efine/PycharmProjects/dataanalysis/Data/trenddata.xlsx'  # CSV location of audit
        writer = pd.ExcelWriter(trendfile, engine='xlsxwriter')
        audit_table = pd.read_excel(trendfile)
        appended_audit = audit_table.append(df, sort=False)  # Add new audit to existing log
        appended_audit.to_excel(writer, sheet_name='Audit', index=False)  # Save audit file
        print("Saving Updated File with New Data")

        writer.save()
        writer.close()

    ##################################################################################
    def clean(self, df):
        df = df.replace(to_replace=r'&#39;', value="'", regex=True) # Replace characters
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
        trendfile = 'C:/Users/efine/PycharmProjects/dataanalysis/Data/trenddata.xlsx'
        old_table = pd.read_excel(trendfile)
        old_set = set(old_table["URL"])
        realtime_set = set(df["URL"])
        new = realtime_set-old_set
        new_titles = df[df['URL'].isin(new)]                             # NEW TITLES

        ##################################################################################
        for i, row in old_table.iterrows():
            title = row['Title']
            hashtag = re.sub(r"([A-Za-z0-9!@#$%^&*()]+)", r"#\1", title)
            hashtag = re.sub(r",", r"", hashtag)
            old_table.at[i, 'Hashtag'] = hashtag

        ##################################################################################
        writer = pd.ExcelWriter(trendfile, engine='xlsxwriter')          # Initiate writer
        updated_table = old_table.append(new_titles, sort=False)         # Add new to old titles, false keeps col order
        updated_table.to_excel(writer, sheet_name='Audit', index=False)  # Save audit file
        writer.save()
        writer.close()
        print("Trend File has been updated with%3d new titles" % (len(new_titles)))

    ##################################################################################

##################################################################################
# MAIN

pytrend = MyTrendReq()
rt = pytrend.real_time_data()
df = pytrend.build(rt)
df = pytrend.clean(df)
print("Real time count: ", len(df.sort_values(by='timesort', ascending=False)))
# pytrend.update(df)                                                          # Only run once to create baseline
df = pytrend.compare(df)
