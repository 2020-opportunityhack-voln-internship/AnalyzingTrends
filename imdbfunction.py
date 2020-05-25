from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re


class ImdbFunction :

    def getIMDB(self, q) :
 
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

        return imdbLinkList[:10]
        
#test = ImdbFunction.getIMDB(0, 'gravity')
#print(test)