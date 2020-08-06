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
        pool = ThreadPool(processes=5)
        
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
        try:
            imThread = pool.apply_async(imdbFunction.getIMDB, (q, size))
            print('started imdb thread')
        except: 
            print('could not find imdb')
            i = []
        rThread = pool.apply_async(redditFunction.getPushshiftData, (100, (dt.date.today() - dt.timedelta(days = (731))),(dt.date.today()), q, size, genType))
        #------Start Curriculum Threads--------#
        aThread = pool.apply_async(scrapeFunction.scrapWebsite, (q, 'askdruniverse', size,genType))
        teThread = pool.apply_async(scrapeFunction.scrapWebsite, (q, 'teachengineering', size,genType))
        
        print('started initial threads')
        #get URLs from IMDb, Wikipedia, Youtube, Steam, and Twitter
        try:
            w = wikipediaFunction.getWiki(q, size)
            print('got wikipedia')
        except:
            print('could not find wikipedia')
            w=[]
        try:
            y = youtubeFunction.getYouTube(q, size)
            print('got youtube')
        except:
            print('could not find youtube')
            y=[]
        try:
            i = imThread.get()
            print('got first imdb thread')
        except:
            print('could not find first imdb thread')
            i=[]
        iThread = pool.apply_async(imdbFunction.getIMDBData, (i, 'dummy'))
        print('started second imdb thread')
        try:
            s = steamFunction.getSteam(q, size)
            print('got steam')
        except:
            print('could not find steam')
            s=[]
        try:
            r = rThread.get()
            print('got reddit')
        except:
            print('could not find reddit')
            r=[]
        
        t=[]
        try:
            ttuples = twitterFunction.getTwitter(q, size)
            print('got twitter')
            for a_tuple in ttuples:
                t.append(a_tuple[0])
        except:
            print('could not find twitter')
            ttuples=[]
        try:
            tw,tw_ids = twitchFunction.getTwitch(q, size)
            print('got twitch')
        except:
            print('could not find twitch')
            tw=[]
            tw_ids=[]
        try:
            tr = trendsFunction.getTrends(q, genType)
            print('got trends')
        except:
            print('could not find trends')
            tr=[]
        try:
            n = nasaFunction.NasaScraper(q, size)
            print('got nasa')
        except:
            print('could not find nasa')
            n=[]
        
        #-------- Get Curriculum Threads -----------#
        try:
            a = aThread.get()
            print('got askdruniverse')
        except:
            print('could not find askdruniverse')
            a=[]
        try:
            te = teThread.get()
            print('got teachengineering') 
        except:
            print('could not find teachengineering')
            te=[]

        
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
        print(te)
        print(a)
        
        print('starting data')
        #----------- Get Link Data -----------#
        #get pageview data from Wikipedia
        try:
            wdata = wikipediaFunction.getWikiData(w)
            print('got wiki data')
        except:
            wdata=[]
        #get Title, Cumulative Worldwide Box Office Gross, Rating, number of Ratings from IMDb
        try:
            idata = iThread.get()
            print('got imdb data')
        except:
            print('could not find imdb data')
            idata=[]
        #get Twitter Likes for posts
        try:
            tdata = ttuples
            print('got twitter data')
        except:
            print('could not find twitter data')
            tdata=[]
        #get Steam player data
        try:
            sdata = steamFunction.getSteamData(s)
            print('got steam data')
        except:
            print('could not find steamdata')
            sdata=[]
        #get Twitch data
        try:
            twdata = twitchFunction.getTwitchData(tw_ids)
            print('got twitch data')
        except:
            print('could not find twitch data')
            twdata=[]
        

        

        
        #----------- Merge URL lists-----------#
        mylist = r + i + w + y + s + t + tw + tr + te + a + n
        
        #----------- Output Links to CSV -----------#
        csvOutput.csvwrite(mylist, q, genType)
        #----------- Generate Graphs -----------#
        print('starting graphs')
        
        try:
            wikipediaFunction.getWikiGraph(wdata, q, genType)
        except:
            print('could not find wikipedia graph')
        try:
            steamFunction.getSteamGraph(sdata, q, genType)
        except:
            print('could not find steam graph')
        try:
            imdbFunction.getIMDBGraph(idata, q, genType)
            print('got imdb graph')
        except:
            print('could not find imdbgraph')
        try:
            twitchFunction.getTwitchGraph(twdata, q, genType)
        except:
            print('could not find twitch graph')
        print('finished graphs')
        return('Finished')
    
    

    # tic = time.perf_counter()
    #app(0,'virus',5,'query')
    # toc = time.perf_counter()
    # print(f"did the thing in {toc - tic:0.4f} seconds")