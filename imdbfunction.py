from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re
#import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
            #find block that contains grossing data            
            yikesGross = soup.find_all('div', class_='txt-block')
            print(url)
            try :
                ratingstring = soup.find('div', class_='imdbRating').getText().split()
                rating=ratingstring[0].replace('/10','')
                ratingCount=int(ratingstring[1].replace(',',''))
            
            except :
                rating = 0
                ratingCount = 0
            #find grossing data in block
            for line in yikesGross:
                if line.find(text=re.compile("Gross")):
                    theline = line
            #find movie title
            title = soup.find('title').getText().replace(' - IMDb','').replace(' ','\n')
            #Try getting text, may otherwise fail if IMDb page does not have data listed
            try :
                mything=theline.getText()
                gross = int(mything.split('$')[1].replace(',','').strip())
                IMDBDataList.append((title,gross,rating,ratingCount))
            except:
                IMDBDataList.append((title, 0 ,rating,ratingCount))
        #returns a tuple in format (TITLE, GROSS, RATING, RATING COUNT)
        return IMDBDataList
        
        #toc = time.perf_counter()
        #print(f"did the thing in {toc - tic:0.4f} seconds")
        
    def getIMDBGraph(self, idata, q) :
        df = pd.DataFrame(idata, columns=['Title','Gross','Rating','Rating Count'])
        df.plot.bar(x='Title',y=['Gross'],rot=0,fontsize='small',title='Movie Popularity Comparison').set_ylabel('Gross Box Office Revenue($)')
        ax2 = df['Rating Count'].plot(secondary_y=True, marker='o', color='red')
        ax2.set_ylabel('Rating Count')
        ax2.legend()
        filename = q.replace(' ','_')
        plt.savefig('imdb_' + str(filename)+'.png',bbox_inches='tight')
        plt.show()

# q = 'space'
# # i = ['https://www.imdb.com/title/tt1355644/', 'https://www.imdb.com/title/tt2239822/']
# i=ImdbFunction.getIMDB(0,q,5)
# idata=ImdbFunction.getIMDBData(0,i)
# ImdbFunction.getIMDBGraph(0,idata,q)



