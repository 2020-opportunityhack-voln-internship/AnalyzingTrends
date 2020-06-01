from twitterscraper import query_tweets
import datetime as dt

list_of_tweets = query_tweets('gravity min_replies:200 min_faves:280 min_retweets:280',10, dt.date(2018, 5, 31), dt.date.today(),15)

sorted_list_of_tweets = sorted(list_of_tweets, key=lambda tweet: tweet.likes, reverse=True)

TweetLinkList = []

for tweet in sorted_list_of_tweets :
    print(tweet.tweet_url.encode('utf-8'))
    print(tweet.likes)
    TweetLinkList.append('https://www.twitter.com' + tweet.tweet_url)
print(TweetLinkList)

