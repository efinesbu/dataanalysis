import re
import numpy as np
import pandas as pd
##################################################################################
# INCREASE DEFAULT COLUMN VISIBILITY

desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 26)
pd.set_option('display.max_rows', 100)
# pop = {'Nevada': {2001: 'ABC', 2002: 2.9},
#        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
# }
# frame = pd.DataFrame(pop).sort_index(0)
# print(frame)
#
# pdata = {'Ohio': frame['Ohio'][:-1],
#          'Nevada': frame['Nevada']}
#
# print(pd.DataFrame(pdata))

# df = pd.DataFrame({'A': ['bat', 'fooo&#39;ooo', 'bait'],
#                    'B': ['abc', 'bar', 'ertwert&#39;sdfs sdfds&#39;sdf &#39;&#39;&#39;']})
# df = df.replace(to_replace=r'&#39;', value="'", regex=True)
# print(df)


# data = "Opioid, Medicine, Chronic pain"
#
# print(data)
#
# array = re.sub(r"([A-Za-z0-9!@#$%^&*()]+)", r"#\1", data)
# array = re.sub(r",", r"", array)
# # print(p)
# print(array)
# print(array[6])
# print(array[7])
# print(array[8])
# print(array[9])
# print(array[10])

trendfile = 'C:/Users/efine/PycharmProjects/dataanalysis/Data/trenddata.xlsx'
old_table = pd.read_excel(trendfile)


for i, row in old_table.iterrows():
    title = row['Title']
    hashtag = re.sub(r"([A-Za-z0-9!@#$%^&*()]+)", r"#\1", title)
    hashtag = re.sub(r",", r"", hashtag)
    old_table.at[i, 'Hashtag'] = hashtag



print(old_table)
# for row in old_table.iterrows():
#     print(row)

# print(old_table)




'''
emil
john,
ben4
hen
'''