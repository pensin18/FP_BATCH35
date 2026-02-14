import datetime

all_days = []
first_day = datetime.datetime(2024,1,1)
for i in range(366):
    all_days.append(first_day)
    first_day += datetime.timedelta(days=1)
# print(all_days)

import datetime as dt

# a = 1769866207
# dt1 = dt.datetime.fromtimestamp(a)
# print(dt1)

# c = dt.datetime.now()
# epoch1 = c.timestamp()
# print(epoch1)


# # convert string to datetime

# a = '2023-01-01'
# f = '%Y-%m-%d'
# dt1 = dt.datetime.strptime(a,f)

# print(dt1)

import pandas as pd
import requests

d1 = pd.read_html('https://groww.in/p/nse-holidays')
print(d1[0])