from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re
#import time

class ImdbFunction :

    def getIMDB(self, q, size) :
 
        queryi = q.replace(" ","-")
        url = ('https://www.imdb.com/search/keyword/?keywords=' + str(queryi) + '&ref_=fn_kw_kw_1&mode=detail&page=1&sort=moviemeter,asc')
        resp = requests.get(url)
        http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
        encoding = html_encoding or http_encoding
        soup = BeautifulSoup(resp.content, from_encoding=encoding,features="lxml")
        print(url)
        
        imdbLinkList = []
        
        #find links to titles
        for link in soup.find_all('a', href= re.compile('title')) :
            #remove irrelevant links
            if "vote" not in link['href'] and "search" not in link['href'] and "plotsummary" not in link['href'] :
                #remove duplicates
                if('https://www.imdb.com' + link['href'] not in imdbLinkList) :
                    imdbLinkList.append('https://www.imdb.com' + link['href'])

        return imdbLinkList[:size]
        
    #test = ImdbFunction.getIMDB(0, 'gravity')
    #print(test)

    def getIMDBData(self, i) :
        #tic = time.perf_counter()
        IMDBDataList = []
        for url in i :
            resp = requests.get(url)
            http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
            html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
            encoding = html_encoding or http_encoding
            soup = BeautifulSoup(resp.content, from_encoding=encoding,features="lxml")
            yikesGross = soup.find_all('div', class_='txt-block')
            
            for line in yikesGross:
                if line.find(text=re.compile("Gross")):
                    theline = line
            
            mything=theline.getText()
            gross = mything.split('$')[1].replace(',','').strip()
            title = soup.find('title').getText().replace(' - IMDb','')
            IMDBDataList.append((title,gross))
        return IMDBDataList
        
        #toc = time.perf_counter()
        #print(f"did the thing in {toc - tic:0.4f} seconds")
        
        
        
    #i = ['https://www.imdb.com/title/tt0816692/', 'https://www.imdb.com/title/tt1355644/', 'https://www.imdb.com/title/tt2239822/']
    #print(getIMDBData(0,i))