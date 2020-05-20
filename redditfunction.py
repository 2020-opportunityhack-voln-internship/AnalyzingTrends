# -*- coding: utf-8 -*-
import requests
import json

class RedditFunction :
    
    #This function returns a list of reddit post links
    def getPushshiftData(self, size, after, before, queryr) :
        url = 'https://api.pushshift.io/reddit/search/submission/?&sort=desc&sort_type=score&over_18=false&score=>2000&size=' +str(size) + '&after=' + str(after) + '&before=' +str(before) + '&q=' + str(queryr)
        
        print(url)
    
        r=requests.get(url)
        data = json.loads(r.text)
        
        fulllinks = []
        
        for var in data['data'] :
            fulllinks.append(var['full_link'])
            
        return fulllinks
   