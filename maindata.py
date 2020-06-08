# -*- coding: utf-8 -*-
from redditfunction import RedditFunction
from imdbfunction import ImdbFunction
from csvoutput import CsvOutput
from wikipediafunction import WikipediaFunction
from youtubefunction import YoutubeFunction
import web_scraper as webScraper


redditFunction = RedditFunction()
imdbFunction = ImdbFunction()
csvOutput = CsvOutput()
wikipediaFunction = WikipediaFunction()
youtubeFunction = YoutubeFunction()

#input string
q = 'gravity'

websites = ['askdruniverse', 'teachengineering']

# scrap the website for the search query
for website in websites:
    webScraper.scrapWebsite(q, website)

#adapt string for reddit or imdb query
queryr = q.replace(" ","+")
queryi = q.replace(" ","-")
queryw = q.replace(" ","+")
queryy = q.replace(" ","+")

r = redditFunction.getPushshiftData(10, 1526428800,1589587200, queryr)
i = imdbFunction.getIMDB(queryi)
w = wikipediaFunction.getWiki(10, queryw)
y = youtubeFunction.getYouTube(queryy)

#URL lists
print(r)
print(i)
print(w)
print(y)
mylist = r + i + w + y

csvOutput.csvwrite(mylist)
