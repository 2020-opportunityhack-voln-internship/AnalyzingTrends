# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re

class YoutubeFunction :
    #This function returns a list of youtube video URLs
    def getYouTube(self, q, size) :
        
            #adapt URL for YouTube query
            queryy = q.replace(" ","+")
            #build url with search query and filter for view count using URI parameter &sp=CAM%253D
            url = ('https://www.youtube.com/results?search_query=' +str(queryy) + '&sp=CAM%253D')
            resp = requests.get(url)
            http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
            html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
            encoding = html_encoding or http_encoding
            soup = BeautifulSoup(resp.content, from_encoding=encoding,features="lxml")

            ytLinkList = []
            print(url)
            ugly = soup.find_all('script')
            for script in ugly:
                if 'videoId' in script.text:
                    myscript = script.text
                    videoIDs = re.findall('watch\?v\=(\w+)',myscript)
                    for video in videoIDs:
                        link = 'https://www.youtube.com/watch?v='+str(video)
                        if len(link) == 43:
                            ytLinkList.append(link)

            return ytLinkList[:size]


#test = YoutubeFunction.getYouTube(0, 'gravity', 10)
#print(test)
 

      
