# -*- coding: utf-8 -*-
import csv

class CsvOutput :
    #This function exports a list to a csv file
    def csvwrite(self, mylist) :
        with open('myfile.csv','w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(mylist)
    
mylist = ['1','2','3']
CsvOutput.csvwrite(0, mylist)