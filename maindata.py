# -*- coding: utf-8 -*-
from redditgraph import RedditFunction
from imdbfunction import ImdbFunction
from csvoutput import CsvOutput
from wikipediafunction import WikipediaFunction
from youtubefunction import YoutubeFunction
from steamfunction import SteamFunction
from twitterfunction import TwitterFunction
from Twitch import TwitchFunction
from trendsfunction import TrendsFunction
import time
import datetime as dt
from multiprocessing.pool import ThreadPool
from websites_scraper import ScrapeFunction
from webscraper import NasaFunction

class AppFunction:
    def app(self, q,size,genType):
        pool = ThreadPool(processes=3)
        
        #----------- Initialize Class Objects -----------#
        redditFunction = RedditFunction()
        imdbFunction = ImdbFunction()
        csvOutput = CsvOutput()
        wikipediaFunction = WikipediaFunction()
        youtubeFunction = YoutubeFunction()
        steamFunction = SteamFunction()
        twitterFunction = TwitterFunction()
        twitchFunction = TwitchFunction()
        trendsFunction = TrendsFunction()
        scrapeFunction = ScrapeFunction()
        nasaFunction = NasaFunction()


        #tic = time.perf_counter()
        print('starting')
        #----------- Call Link Fetch Functions -----------#
        #Run reddit in seperate thread to reduce execution time
        rThread = pool.apply_async(redditFunction.getPushshiftData, (100, (dt.date.today() - dt.timedelta(days = (731))),(dt.date.today()), q, size, genType))
        #------Start Curriculum Threads--------#
        aThread = pool.apply_async(scrapeFunction.scrapWebsite, (q, 'askdruniverse', size,genType))
        teThread = pool.apply_async(scrapeFunction.scrapWebsite, (q, 'teachengineering', size,genType))
        print('started initial threads')
        #get URLs from IMDb, Wikipedia, Youtube, Steam, and Twitter
        i = imdbFunction.getIMDB(q, size)
        print('got imdb')
        w = wikipediaFunction.getWiki(q, size)
        print('got wikipedia')
        y = youtubeFunction.getYouTube(q, size)
        print('got youtube')
        s = steamFunction.getSteam(q, size)
        t=[]
        ttuples = twitterFunction.getTwitter(q, size)
        print('got twitter')
        for a_tuple in ttuples:
            t.append(a_tuple[0])
        tw,tw_ids = twitchFunction.getTwitch(q, size)
        print('got twitch')
        tr = trendsFunction.getTrends(q, genType)
        print('got trends')
        n = nasaFunction.NasaScraper(q, size)
        print('got nasa')
        #get thread running for reddit's output
        r = rThread.get()
        print('got reddit')
        
        #toc = time.perf_counter()
        #print(f"did the thing in {toc - tic:0.4f} seconds")
        
        

        #URL lists
        print(r)
        print(i)
        print(w)
        print(y)
        print(s)
        print(t)
        print(tw)
        print(tr)
        print(n)
 
        print('starting data')
        #----------- Get Link Data -----------#
        #get pageview data from Wikipedia
        wdata = wikipediaFunction.getWikiData(w)
        #get Title, Cumulative Worldwide Box Office Gross, Rating, number of Ratings from IMDb
        idata = imdbFunction.getIMDBData(i)
        #get Twitter Likes for posts
        tdata = ttuples
        #get Steam player data
        sdata = steamFunction.getSteamData(s)
        #get Twitch data
        twdata = twitchFunction.getTwitchData(tw_ids)
        print('got data')
        
        #-------- Get Curriculum Threads -----------#
        a = aThread.get()
        print('finished askdruniverse')
        te = teThread.get()
        print('finished teachengineering')  
        
        print(te)
        print(a)
        
        #----------- Merge URL lists-----------#
        mylist = r + i + w + y + s + t + tw + tr + te + a + n
        
        #----------- Output Links to CSV -----------#
        csvOutput.csvwrite(mylist, q, genType)
        #----------- Generate Graphs -----------#
        wikipediaFunction.getWikiGraph(wdata, q, genType)
        steamFunction.getSteamGraph(sdata, q, genType)
        imdbFunction.getIMDBGraph(idata, q, genType)
        twitchFunction.getTwitchGraph(twdata, q, genType)
        return('Finished')
    
    

    
    #app(0,'gravity',5,'query')