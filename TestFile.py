import re
import numpy as np
import pandas as pd

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
}
frame = pd.DataFrame(pop).sort_index(0)
print(frame)

pdata = {'Ohio': frame['Ohio'][:-1],
         'Nevada': frame['Nevada']}

print(pd.DataFrame(pdata))



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