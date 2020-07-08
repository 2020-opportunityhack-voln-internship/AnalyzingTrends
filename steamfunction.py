# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re
import matplotlib.pyplot as plt
import pandas as pd

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

    def getSteamData(self, s) :
        SteamData = {}
        monthslength = 0
        months = []
        i=0
        for url in s :
            try:
                testmonths = []
                peaks = []
                app = url.replace('https://store.steampowered.com','https://steamcharts.com')[0:35]
                resp=requests.get(app)
                http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
                html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
                encoding = html_encoding or http_encoding
                soup = BeautifulSoup(resp.content, from_encoding=encoding,features="lxml")
                title = soup.find('h1').getText()
                yikesMonths=soup.find_all('td',class_='month-cell left')
                yikesPeak=soup.find_all('td',class_='right num')
                
                for point in yikesPeak :
                    peak = int(point.getText())
                    peaks.append(peak)
                for point in yikesMonths :
                    month = point.getText().replace('\n','').replace('\t','')
                    testmonths.append(month)
                testmonths = testmonths[0:24]
                if len(testmonths) > monthslength:
                    months = testmonths
                    monthslength = len(months)
                peaks = peaks[0:24]
                months = months
                SteamData[title]=(peaks)
                SteamData['Date']=(months)
            except:
                SteamData[i] = ([0])
                i = i+1
        for i, j in SteamData.items():
            if len(j) < monthslength:
                   # j[0:0] = ([0] * (monthslength - len(j)))
                  j.extend(([0] * (monthslength - len(j))))
                 #print(i, len(j))
        for key, values in SteamData.items() :
            key = values.reverse()
        return SteamData

    def getSteamGraph(self, sdata, q) :
        df = pd.DataFrame.from_dict(sdata)
        df = df.set_index('Date')
        plot = df.plot(fontsize = 'small', title = 'Game Popularity Comparison',legend=None).set_ylabel('Peak Monthly Playercount')
        plt.figlegend(bbox_to_anchor=(1.35,1),
                           bbox_transform=plt.gcf().transFigure)
        filename = q.replace(' ','_')
        plt.savefig('steam_' + str(filename)+'.png',bbox_inches='tight')
# q = 'space'
# s = SteamFunction.getSteam(0, q ,3)
# # s = ('https://store.steampowered.com/app/952060/Resident_Evil_3/','https://store.steampowered.com/app/244850/Space_Engineers/')
# sdata = SteamFunction.getSteamData(0, s)
# SteamFunction.getSteamGraph(0, sdata, q)