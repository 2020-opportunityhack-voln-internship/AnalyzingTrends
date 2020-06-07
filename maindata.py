# -*- coding: utf-8 -*-
from redditfunction import RedditFunction
from imdbfunction import ImdbFunction
from csvoutput import CsvOutput
from wikipediafunction import WikipediaFunction
from youtubefunction import YoutubeFunction
from steamfunction import SteamFunction
from twitterfunction import TwitterFunction
#import time
from multiprocessing.pool import ThreadPool

pool = ThreadPool(processes=1)

redditFunction = RedditFunction()
imdbFunction = ImdbFunction()
csvOutput = CsvOutput()
wikipediaFunction = WikipediaFunction()
youtubeFunction = YoutubeFunction()
steamFunction = SteamFunction()
twitterFunction = TwitterFunction()
#input string
q = 'gravity'
size = 3
#tic = time.perf_counter()

#Run reddit in seperate thread to reduce execution time
rThread = pool.apply_async(redditFunction.getPushshiftData, (100, 1526428800,1589587200, q, size))

i = imdbFunction.getIMDB(q, size)
w = wikipediaFunction.getWiki(q, size)
y = youtubeFunction.getYouTube(q, size)
s = steamFunction.getSteam(q, size)
t=[]
ttuples = twitterFunction.getTwitter(q, size)
for a_tuple in ttuples:
    t.append(a_tuple[0])
    
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
print(t)
mylist = r + i + w + y + s + t

csvOutput.csvwrite(mylist, q)

wdata = wikipediaFunction.getWikiData(w)
idata = imdbFunction.getIMDBData(i)
tdata = ttuples