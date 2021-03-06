# -*- coding: utf-8 -*-
import csv

class CsvOpener:

    def CsvOpen(self,genType,q) :
        q = q.replace(' ','_')
        if genType == 'query':
            file = 'query/query.csv'
        elif genType == 'suggested':
            file = 'suggested/'+str(q) +'.csv'

        
        rlinks=""
        tlinks=""
        slinks=""
        wlinks=""
        ylinks=""
        ilinks=""
        twlinks=""
        trlinks=""
        telinks=""
        alinks=""
        nlinks=""
        
        with open('static/linklists/'+str(file), newline='') as csvfile:
            links = list(csv.reader(csvfile, delimiter = ','))[0]
            for link in links:
                link = '<li><a href="'+str(link)+'" target="_blank">'+str(link)+'</a></li>'
                if 'reddit.com' in link:
                    rlinks = rlinks + str(link)
                if 'twitter.com' in link:
                    tlinks = tlinks + str(link)
                if 'steampowered.com' in link:
                    slinks = slinks + str(link)
                if 'wikipedia.org' in link:
                    wlinks = wlinks + str(link)
                if 'youtube.com' in link:
                    ylinks = ylinks + str(link)
                if 'imdb.com' in link:
                    ilinks = ilinks + str(link)
                if 'twitch.tv' in link:
                    twlinks = twlinks + str(link)
                if 'trends.google.com' in link:
                    trlinks = trlinks + str(link)
                if 'teachengineering' in link:
                    telinks = telinks + str(link)
                if 'askdruniverse' in link:
                    alinks = alinks + str(link)
                if 'nasa.gov' in link:
                    nlinks = nlinks + str(link)
            
        return rlinks,tlinks,slinks,wlinks,ylinks,ilinks,twlinks, trlinks, telinks, alinks, nlinks
        
#linkinfo = CsvOpener.CsvOpen(0,'query','gravity')
#ilinkstest = linkinfo[5]