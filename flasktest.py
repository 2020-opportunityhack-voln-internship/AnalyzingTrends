# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,Markup
from maindata import AppFunction
from random import random
from csvopener import CsvOpener
appFunction = AppFunction()
csvOpener = CsvOpener()
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

    
@app.route('/')
def picture():
    message = 'Welcome!'
    return render_template('index.html',message=message)

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
    print(ilinks)
    return render_template('return_form.html',processed_size=processed_size,processed_text=processed_text,random=randomn,imdblinks=ilinks,wikilinks=wlinks,steamlinks=slinks,redditlinks=rlinks,twitterlinks=tlinks,youlinks=ylinks,twitchlinks = twlinks,trendlinks = trlinks)

if __name__ == "__main__":
    app.run(host="localhost", port=int("777"),debug=True,use_reloader=False)
