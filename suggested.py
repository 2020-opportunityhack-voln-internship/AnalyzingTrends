# -*- coding: utf-8 -*-
from maindata import AppFunction
import time

class SuggestedFunction:

    suggestedlist = [
        'gravity',
        'electron',
        'space'
        ]
    
    def load_suggested(self):
        
        for item in SuggestedFunction.suggestedlist:
            AppFunction.app(0, item, 5, 'suggested')
            time.sleep(15)
    
    def suggested_html(self):
        suggestedhtmllist = []
        for item in SuggestedFunction.suggestedlist:
            item = "<option value =\"" + str(item) + "\">" + str(item) + "</option>"
            suggestedhtmllist.append(item)
        return suggestedhtmllist
    

    
#test = SuggestedFunction.suggested_html()
#print(test)