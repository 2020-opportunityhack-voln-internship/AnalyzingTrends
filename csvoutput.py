# -*- coding: utf-8 -*-
import csv

class CsvOutput :
    #This function exports a list to a csv file
    def csvwrite(self, mylist, q) :
       #generate uniquely named files
        queryc = q.replace(" ","-")
       #overwrite existing csv file
        #queryc = 'default'
        with open(str(queryc) + '.csv','w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(mylist)
    
#mylist = ['1','2','3']
#CsvOutput.csvwrite(0, mylist)