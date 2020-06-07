# -*- coding: utf-8 -*-
import requests
import json

class RedditFunction :
    
    #This function returns a list of reddit post links
    def getPushshiftData(self, results, after, before, q, size) :
        queryr = q.replace(" ","+")
        args = '&sort=desc&sort_type=score&over_18=false&score=>2000&size=' +str(results) + '&after=' + str(after) + '&before=' +str(before) + '&q=' + str(queryr)
        url = 'https://api.pushshift.io/reddit/search/submission/?' +str(args)
        print(url)
    
        r=requests.get(url)
        data = json.loads(r.text)
        
        fulllinks = []
        
        for post in data['data'] :
            fulllinks.append(post['full_link'])
            
        return fulllinks[:size]
#test = RedditFunction.getPushshiftData(0, 100 ,1526428800,1589587200, 'gravity', 10)
#print(test)