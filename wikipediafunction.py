# -*- coding: utf-8 -*-
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
#from datetime import date
class WikipediaFunction :
    
    #This function returns a list of wikipedia article links
    def getWiki(self, q, size) :
        queryw = q.replace(" ","+")
        args = '?action=opensearch&search=' + str(queryw) +'&limit=' +str(size) + '&namespace=0&format=json'
        url =  'https://en.wikipedia.org/w/api.php' + str(args)
        print(url)
        
        w=requests.get(url)
        data = json.loads(w.text)
        links = data[3]
        return links
    #test = getWiki(0, 10, 'quantum+mechanics')
    #print(test)
    
    #This function retrieves monthly pageview date for a given URL list of wikipedia articles
    def getWikiData(self, w) :
        
        #extract page title from url
        pagetitles = [x.replace('https://en.wikipedia.org/wiki/','') for x in w]
        #empty dictionary to be populated
        wikidict = {}
        #today's date in wikipedia's required format
        before = (datetime.today().strftime('%Y%m%d'))
        y = datetime.today() 
        z = y.replace(year = y.year - 2)
        #the date 2 years ago with wikipedia's required formate
        after = z.strftime('%Y%m%d')

        #retrieve date for each page title in list
        for pagetitle in pagetitles :
            url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/' +str(pagetitle) + '/monthly/' + str(after) + '/'+ str(before)
            print(url)
            response = requests.get(url)
            data = json.loads(response.text)
            items = data.get('items')
            
            #only place variables of interest into dictionary
            wikidata = [(point['views'],point['timestamp']) for point in items]
            #add data to dictionary with key = pagetitle
            wikidict[pagetitle] = wikidata
        return wikidict
    
    #This function produces two graphs for monthly pageview date for a given dictionary of data
    def getWikiGraph(self, wdata, q) :
        #initial value to compare list lengths against
        maxlength = 0
        #initialize empty dictionary
        newdict ={}
        #find longest list of data in dictionary
        for pagetitle, points in wdata.items():
            if len(points) > maxlength :
                maxlength = len(points)
        #unwrap wanted data from tuples
        for pagetitle, points in wdata.items():
            #use date column for the longest (oldest) entry
            date = [i[1] for i in points]
            if len(date) == maxlength :
                newdict['Date'] = date  
            values = [i[0] for i in points]
            #pad all lists of pageview data with 0s to match column length of oldest entry to ready for conversion to dataframe
            if len(values) < maxlength:
                values[0:0] = [0] * (maxlength - len(values))
            newdict[pagetitle] = values
        #make .png filename match query
        filename = q.replace(" ","_")
        #convert dictionary to pandas dataframe
        df = pd.DataFrame.from_dict(newdict)
        #make date index column, better for graphing
        df = df.set_index('Date')
        #plot first graph using subplots
        plot = df.plot(subplots=True,legend=None)
        plt.title('Monthly Wikipedia Pageviews', y=len(wdata)+len(wdata)/5)
        #plt.tight_layout
        plt.figlegend(bbox_to_anchor=(1.4,1))
        plt.savefig('wiki_'+str(filename)+'.png',bbox_inches='tight')
        #plot second graph without subplots
        df.plot()
        plt.title('Monthly Wikipedia Pageviews')
        plt.legend(bbox_to_anchor=(.9,.75),
                   bbox_transform=plt.gcf().transFigure)
        plt.savefig('wiki_' + str(filename)+'1.png',bbox_inches='tight')
        plt.show()
# w = WikipediaFunction.getWiki(0, 'space',5)
# wdata = WikipediaFunction.getWikiData(0,w)
# WikipediaFunction.getWikiGraph(0,wdata,'space')
