# -*- coding: utf-8 -*-
from redditfunction import RedditFunction
from imdbfunction import ImdbFunction
from csvoutput import CsvOutput
from wikipediafunction import WikipediaFunction
from youtubefunction import YoutubeFunction
from steamfunction import SteamFunction
#import time
from multiprocessing.pool import ThreadPool

pool = ThreadPool(processes=1)

redditFunction = RedditFunction()
imdbFunction = ImdbFunction()
csvOutput = CsvOutput()
wikipediaFunction = WikipediaFunction()
youtubeFunction = YoutubeFunction()
steamFunction = SteamFunction()

#input string
q = 'gravity'

#tic = time.perf_counter()

#Run reddit in seperate thread to reduce execution time
rThread = pool.apply_async(redditFunction.getPushshiftData, (100, 1526428800,1589587200, q))

i = imdbFunction.getIMDB(q)
w = wikipediaFunction.getWiki(10, q)
y = youtubeFunction.getYouTube(q)
s = steamFunction.getSteam(q)

#get thread running for reddit's output
r = rThread.get()

#toc = time.perf_counter()
#print(f"did the thing in {toc - tic:0.4f} seconds")

#URL lists
print(r)
print(i)
print(w)
print(y)
print(s)
mylist = r + i + w + y + s

csvOutput.csvwrite(mylist, q)