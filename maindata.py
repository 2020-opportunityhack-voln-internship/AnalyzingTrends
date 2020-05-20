# -*- coding: utf-8 -*-
from redditfunction import RedditFunction
from imdbfunction import ImdbFunction
from csvoutput import CsvOutput

redditFunction = RedditFunction()
imdbFunction = ImdbFunction()
csvOutput = CsvOutput()

#input string
q = 'pulley'

#adapt string for reddit or imdb query
queryr = q.replace(" ","+")
queryi = q.replace(" ","-")

r = redditFunction.getPushshiftData(10, 1526428800,1589587200, queryr)
i = imdbFunction.getIMDB(queryi)

#URL lists
print(r)
print(i)

mylist = r + i

csvOutput.csvwrite(mylist)