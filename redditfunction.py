# -*- coding: utf-8 -*-
import requests
import json

class RedditFunction :
    
    #This function returns a list of reddit post links
    def getPushshiftData(self, size, after, before, queryr) :
        args = '&sort=desc&sort_type=score&over_18=false&score=>2000&size=' +str(size) + '&after=' + str(after) + '&before=' +str(before) + '&q=' + str(queryr)
        url = 'https://api.pushshift.io/reddit/search/submission/?' +str(args)
        print(url)
    
        r=requests.get(url)
        data = json.loads(r.text)
        
        fulllinks = []
        
        for post in data['data'] :
            fulllinks.append(post['full_link'])
            
        return fulllinks
   