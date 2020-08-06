# -*- coding: utf-8 -*-
import csv

class CsvOutput :
    #This function exports a list to a csv file
    def csvwrite(self, mylist, q, genType) :
       #generate uniquely named files
        queryc = q.replace(" ","-")
        #queryc = 'default'
        if genType=='suggested':
            with open('static/linklists/suggested/'+str(queryc) + '.csv','w', newline='', encoding = "utf-8") as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(mylist)
        if genType=='query':
            with open('static/linklists/query/query.csv','w', newline='', encoding = "utf-8") as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(mylist)
#mylist = ['1','2','3']
#CsvOutput.csvwrite(0, mylist)