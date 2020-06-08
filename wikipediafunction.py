# -*- coding: utf-8 -*-
import requests
import json

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

    def getWikiData(self, w) :
        
        pagetitles = [x.replace('https://en.wikipedia.org/wiki/','') for x in w]
        wikidict = {}
        for pagetitle in pagetitles :
            url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/' +str(pagetitle) + '/monthly/2018050300/2020050300'
            print(url)
            response = requests.get(url)
            data = json.loads(response.text)
            items = data.get('items')
            
            wikidata = [(point['views'],point['timestamp']) for point in items]
            #print(wikidata)
            wikidict[pagetitle] = wikidata
        return wikidict


    #links = ["https://en.wikipedia.org/wiki/Albert_Einstein", "https://en.wikipedia.org/wiki/Gravity","https://en.wikipedia.org/wiki/Fluids"]
    #test = getWikiData(0, links)
    #print(test)
