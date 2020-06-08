# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re


class SteamFunction :

    def getSteam(self, q, size) :
        querys = q.replace(" ","+")
        url = ('https://store.steampowered.com/search/?term=' + str(querys) + '&category1=998')
        resp = requests.get(url)
        http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
        encoding = html_encoding or http_encoding
        soup = BeautifulSoup(resp.content, from_encoding=encoding,features="lxml")
        print(url)
        
        SteamLinkList = []
        
        #find links to apps
        for link in soup.find_all('a', href= re.compile('app')) :
                  #remove duplicates
                if(link['href'] not in SteamLinkList) :
                    SteamLinkList.append(link['href'])

        #remove first two irrelevant links
        return SteamLinkList[2:size+2]

#test = SteamFunction.getSteam(0, 'gravity')
#print(test)


