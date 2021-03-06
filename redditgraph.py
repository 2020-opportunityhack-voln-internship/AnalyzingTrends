import json
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import time
import statistics


class RedditFunction :


    #This function returns a list of reddit post links
    def getPushshiftData(self, results, after, before, q, size, genType) :


        queryr = q.replace(" ","+")
        args = '&sort=desc&sort_type=score&over_18=false&score=>2000&size=' +str(results) + '&after=' + str(after) + '&before=' +str(before) + '&q=' + str(queryr)
        url = 'https://api.pushshift.io/reddit/search/submission/?' +str(args)

        #print("URL = ", url)

        r=requests.get(url)
        data = json.loads(r.text)

        #print(data)

        fulllinks = []



        for post in data['data'] :
            fulllinks.append(post['full_link'])


        posts = []

        # score : number of upvotes
        # num_comments: number of comments
        # created utc: when the post was created
        for post in data['data']:
            posts.append([post['score'], post['num_comments'], post['created_utc'], post['full_link']])




        #print(posts)

        # sorting by upvotes and then comments in reverse order
        #posts.sort(key = lambda x: (x[0], x[2]), reverse = True)

        times=[]
        pops=[]
        for p in posts:
            pops.append(p[0])
            times.append(p[2])

        for t in range(len(times)):
            times[t]=datetime.utcfromtimestamp(times[t]).strftime('%Y-%m-%d')


        rel_data={}

        # making dictionary of {time: scores}
        for t in range(len(times)):
            rel_data[times[t]]=pops[t]

        #print(rel_data)
        times.sort()
        pop_scores=[]
        for time in times:
            pop_scores.append(rel_data[time])

        rel_data_grouped={}
        for date in times:
            short_date = '-'.join(date.split('-')[:2])
            #print(short_date)
            if short_date not in rel_data_grouped:
                rel_data_grouped[short_date]=[]
            rel_data_grouped[short_date].append(rel_data[date])

        final_data={}

        for month in rel_data_grouped:
            final_data[month]=statistics.mean(rel_data_grouped[month])

        newfinal_data={}
        for date in final_data.keys():
            newdate = datetime.strptime(date,'%Y-%m')
            newfinal_data[newdate]=final_data[date]
            
        #current_time = datetime.datetime.now()
        #current_time_utc = datetime.utc()
        #print(current_time, current_time_utc)
        #print(p[0],p[2])
        
        plt.plot(list(newfinal_data.keys()), list(newfinal_data.values()),color='crimson', label = q)
        plt.ylabel('popularity')
        plt.xlabel('time')
        plt.yscale('log')
        plt.xticks(rotation=60)
        plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
        filename = q.replace(' ','_')
        if genType=='suggested':
            plt.savefig('static/images/suggested/reddit_' + str(filename)+'.png',bbox_inches='tight')
        elif genType=='query':
            plt.savefig('static/images/query/reddit.png',bbox_inches='tight')
            
        print('done in reddit thread')
        return fulllinks[:size]
    
#tic = time.perf_counter()
#test = RedditFunction.getPushshiftData(0, 100 ,1526428800,1589587200, 'gravity', 10, 'query')
#toc = time.perf_counter()
#print(f"did the thing in {toc - tic:0.4f} seconds")

# print(test)
