# -*- coding: utf-8 -*-
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
from datetime import datetime

q = 'gravity'

#build query
pytrend = TrendReq()
pytrend.build_payload(kw_list=[q])

#get timeseries data
df = pytrend.interest_over_time()

#create filter for last 2 years
y = datetime.today() 
z = y.replace(year = y.year - 2)
after = z.strftime('%Y%m%d')

#filter and plot data
df = df.query('index > ' + (after))
plot = df.plot()
plt.title('Search Interest Over Time')
plt.ylabel('Relative Interest')
plt.xlabel('Date')
plt.show()

#get related topics

related = pytrend.related_topics()
keys = related.keys()
for key in keys:
    toprelated = related[key]['top'].head(10)
    relatedlist = list(toprelated['topic_title'])
    plot = toprelated.plot(x='topic_title',y='value',kind='bar', legend=None)
    plt.ylabel('Relative Similarity')
    plt.xlabel('Related Topics')
    plt.title('People who searched for ' + str(q) + ' also searched for:')
    plt.show()
    print(relatedlist)