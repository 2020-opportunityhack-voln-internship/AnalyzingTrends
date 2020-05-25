# -*- coding: utf-8 -*-
import requests
import json

class WikipediaFunction :
    
    #This function returns a list of wikipedia article links
    def getWiki(self, size, q) :
        queryw = q.replace(" ","+")
        args = '?action=opensearch&search=' + str(queryw) +'&limit=' +str(size) + '&namespace=0&format=json'
        url =  'https://en.wikipedia.org/w/api.php' + str(args)
        print(url)
        
        w=requests.get(url)
        data = json.loads(w.text)
        links = data[3]
        return links
#test = WikipediaFunction.getWiki(0, 10, 'quantum+mechanics')
#print(test)


