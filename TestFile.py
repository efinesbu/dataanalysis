import re
import numpy as np
import pandas as pd

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

df = pd.DataFrame({'A': ['bat', 'fooo&#39;ooo', 'bait'],
                   'B': ['abc', 'bar', 'ertwert&#39;sdfs sdfds&#39;sdf &#39;&#39;&#39;']})
df = df.replace(to_replace=r'&#39;', value="'", regex=True)
print(df)

'''
data = "asdfasdf"

array = data

print(array[0])

array = re.sub(r"0-9", "0", array)

print(array)
'''



'''
emil
john,
ben4
hen
'''