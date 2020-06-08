from twitterscraper import query_tweets
import datetime as dt

class TwitterFunction:
    
    def getTwitter(self, q, size) :
        #Populary Thresholds:
        #replies to post
        replies = 20
        #favorites
        faves = 150
        #retweets
        retweets = 20
        #begining search date, default 2 years before today
        after = dt.date.today() - dt.timedelta(days = (730))
        #end search date, default today
        before = dt.date.today()
        #number of threads in pool, high numbers return more tweets but increase runtime, recommended <=4
        poolsize = 4
        #adapt query for exact match
        query = '"' + str(q) + '"'
        #max number of tweets found by each thread
        qsize = 10
        #build initial list of tweet objects via scraper
        list_of_tweets = query_tweets(str(query) + ' min_replies:'+str(replies) +' min_faves:' +str(faves) +' min_retweets:'+str(retweets),qsize, after, before, poolsize)
        #sort tweet objects by likes property
        sorted_list_of_tweets = sorted(list_of_tweets, key=lambda tweet: tweet.likes, reverse=True)
        #create empty list to be populated
        TweetLinkList = []
        #add unique tweets to list
        for tweet in sorted_list_of_tweets :
           if (('https://www.twitter.com' + tweet.tweet_url,tweet.likes)) not in TweetLinkList: 
            # print(tweet.tweet_url.encode('utf-8'))
           # print(tweet.likes)
               TweetLinkList.append((('https://www.twitter.com' + tweet.tweet_url),tweet.likes))
               
        return TweetLinkList[:size]
    #test = getTwitter(0,'fluid dynamics',10)
    #print(test)

