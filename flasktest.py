# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,Markup
from maindata import AppFunction
from random import random
from csvopener import CsvOpener
from suggested import SuggestedFunction


appFunction = AppFunction()
csvOpener = CsvOpener()
suggestedFunction = SuggestedFunction()


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

    
@app.route('/')
def landing():

    return render_template('index.html')

@app.route('/form')
def my_form():
    return render_template('my_form.html')

@app.route('/form',methods=['Post'])
def my_form_post():
    q = request.form['text']
    size = int(request.form['size'])
    processed_size = str(size)
    processed_text=q.upper()
    genType='query'
    finished = appFunction.app(q,size,genType)
    randomn = 1 + random() 
    print(finished)
    linkinfo = csvOpener.CsvOpen(genType,q)
    rlinks = Markup(linkinfo[0])
    tlinks = Markup(linkinfo[1])
    slinks = Markup(linkinfo[2])
    wlinks = Markup(linkinfo[3])
    ylinks = Markup(linkinfo[4])
    ilinks = Markup(linkinfo[5])
    twlinks = Markup(linkinfo[6])
    trlinks = Markup(linkinfo[7])
    telinks = Markup(linkinfo[8])
    alinks = Markup(linkinfo[9])
    nlinks = Markup(linkinfo[10])
    location = '/query/'
    qname = ""
    return render_template('return_form.html',processed_size=processed_size,processed_text=processed_text,random=randomn,imdblinks=ilinks,wikilinks=wlinks,steamlinks=slinks,redditlinks=rlinks,twitterlinks=tlinks,youlinks=ylinks,twitchlinks = twlinks,trendlinks = trlinks,location = location, qname = qname, telinks = telinks, alinks = alinks, nlinks = nlinks)

@app.route('/suggested')
def suggested_form():
    suggested_topics = Markup(suggestedFunction.suggested_html())
    return render_template('suggested_form.html',suggested_topics=suggested_topics)
    
@app.route('/suggested',methods=['Post'])
def suggested_form_post():
    q = request.form['topic']
    print('thing is ' + str(q))
    size = 5
    processed_size = str(size)
    processed_text = q.upper()
    genType='suggested'
    linkinfo = csvOpener.CsvOpen(genType,q)
    randomn = 1 + random() 
    rlinks = Markup(linkinfo[0])
    tlinks = Markup(linkinfo[1])
    slinks = Markup(linkinfo[2])
    wlinks = Markup(linkinfo[3])
    ylinks = Markup(linkinfo[4])
    ilinks = Markup(linkinfo[5])
    twlinks = Markup(linkinfo[6])
    trlinks = Markup(linkinfo[7])
    telinks = Markup(linkinfo[8])
    alinks = Markup(linkinfo[9])
    nlinks = Markup(linkinfo[10])
    location = '/suggested/'
    qname = str(q).replace(' ','_')
    qname = '_' + str(qname)
    return render_template('return_form.html',processed_size=processed_size,processed_text=processed_text,random=randomn,imdblinks=ilinks,wikilinks=wlinks,steamlinks=slinks,redditlinks=rlinks,twitterlinks=tlinks,youlinks=ylinks,twitchlinks = twlinks,trendlinks = trlinks,location=location, qname = qname, telinks = telinks, alinks = alinks, nlinks = nlinks)



if __name__ == "__main__":
    app.run(host="localhost", port=int("777"),debug=True,use_reloader=False)
