import requests
import json
import databaseconfig as cfg
import pandas as pd
import matplotlib.pyplot as plt


class TwitchFunction:
 #getTwitch function:Input query and size and Output twitchlinks list and twitchids list
 #twitch ids will be input for getTwitchData function to fetch followers and views count for particular channel id
    def getTwitch(self, q, size) :
        queryi = q.replace(" ","-")
        url1 = 'https://api.twitch.tv/helix/search/channels?query='+str(queryi)+'&first='+str(size)
        headers = {
            "client-id" : cfg.my["client_id"],
            "Authorization": "Bearer "+cfg.my["outh"]
        }
        r = requests.get(url1, headers=headers)
        mydata = json.loads(r.text)
        #print(mydata)
        twitchlinks = []
        twitchid = []
        try:
            for post in mydata['data']:
                if('https://www.twitch.tv/' + post['display_name'] not in twitchlinks) :
                    twitchlinks.append('https://www.twitch.tv/' + post['display_name'])
                    twitchid.append(post['id'])
#             print(twitchid)
        except TypeError:
            print("Sorry for!" + str(err))
            
        return twitchlinks[:size],twitchid[:size]

    def getTwitchData(self,i) :
        TwitchData = []
        for ids in i :
            url1 ='https://api.twitch.tv/kraken/channels/'+ str(ids)
            headers = {
                    "client-id": cfg.my["client_id"],
                    "Accept": "application/vnd.twitchtv.v5+json" }
            r = requests.get(url1, headers=headers)
            twi_data = json.loads(r.text)
            try:
                TwitchData.append(((twi_data['display_name'],twi_data['followers'],twi_data['views'])))
            except TypeError as err:
                    print("Sorry for!" + str(err))
        return TwitchData
    
    def getTwitchGraph(self, idata, q, genType) :
        try:
            df = pd.DataFrame(idata, columns=['Channel','Followers','Views'])
            df.plot.bar(x='Channel',y=['Views'],rot=0,fontsize='small',title='Channel Popularity Comparison').set_ylabel('Views_Count')
            ax2 = df['Followers'].plot(secondary_y=True, marker='o', color='red')
            ax2.set_ylabel('Followers_Count')
            ax2.legend(loc=2)
            filename = q.replace(' ','_')
            if genType=='query':
                plt.savefig('static/images/query/twitch.png',bbox_inches='tight')
   
            if genType=='suggested':
                plt.savefig('static/images/suggested/twitch_' + str(filename)+'.png',bbox_inches='tight')

                plt.show()
        except:
            print("Could not find Twitch data")
            
#q='electron'
#channel,id_s = TwitchFunction.getTwitch(0,q,5)
#channel list and id list are generated
#print(channel)
#i = ['121736069', '161627953', '30872040', '113329225', '223462922']
#id_s list to get twitch data
#idata =TwitchFunction.getTwitchData(0,id_s)
#print(idata)
#generate graph for the query
#TwitchFunction.getTwitchGraph(0,idata,q,'suggested')