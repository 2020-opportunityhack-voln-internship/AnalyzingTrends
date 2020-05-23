# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re

class YoutubeFunction :
    #This function returns a list of youtube video URLs
    def getYouTube(self, queryy) :
        
            url = ('https://www.youtube.com/results?search_query=' +str(queryy) + '&sp=CAMSAhAB')
            resp = requests.get(url)
            http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
            html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
            encoding = html_encoding or http_encoding
            soup = BeautifulSoup(resp.content, from_encoding=encoding,features="lxml")
            print(url)
            
            ytLinkList = []
            
            for link in soup.find_all('a', href= re.compile('watch')) :
                if('https://www.youtube.com/' + link['href'] not in ytLinkList) :
                    ytLinkList.append('https://www.youtube.com/' + link['href'])
                    
            return ytLinkList


#test = YoutubeFunction.getYouTube(0, 'gravity')
#print(test)
 
