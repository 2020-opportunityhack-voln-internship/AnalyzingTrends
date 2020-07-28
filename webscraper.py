from bs4 import BeautifulSoup
import time
from requests import get
import csv
import pandas as pd

links = []
pages = [str(i) for i in range(1,100)]
q = "gravity"

for page in pages:
    print("Page", page)
    time.sleep(2)
    response = get(
        'https://nasasearch.nasa.gov/search?affiliate=nasa&page=' + str(page) + '&query=q&utf8=%E2%9C%93')
    print(response)
    time.sleep(2)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    movie_containers = html_soup.find_all('div', class_='content-block-item result')

    for container in movie_containers:
        link = container.h4.a
        if link and 'href' in link.attrs:
            all_links = link.get('href')
            links.append(all_links)
            print(links)

data = pd.DataFrame({'Urls': links})
data.to_csv('links.csv')
data.drop(data.columns[0], axis=1)
print(len(links))

