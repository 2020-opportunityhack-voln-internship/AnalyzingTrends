from bs4 import BeautifulSoup
import time
from requests import get
import csv
import pandas as pd

class NasaFunction:
    
    def NasaScraper(self, q, size):
        links = []
        pages = '1'
        qs = q.replace(' ','+')

        
        for page in pages:
            print("Page", page)
            response = get(
                'https://nasasearch.nasa.gov/search?affiliate=nasa&page=' + str(page) + '&query=' + str(qs) + '&utf8=%E2%9C%93')
        
            time.sleep(2)
            html_soup = BeautifulSoup(response.text, 'html.parser')
        
            movie_containers = html_soup.find_all('div', class_='content-block-item result')
        
            for container in movie_containers:
                link = container.h4.a
                if link and 'href' in link.attrs:
                    all_links = link.get('href')
                    links.append(all_links)
                    #print(links)
        
        finallinks = []
        for link in links:
            if 'images' not in link:
                finallinks.append(link)
                
        return finallinks[:size]
    
#test = NasaFunction.NasaScraper(0, 'acid',5)
#print(test)

