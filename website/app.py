import flask
import pickle
import numpy as np
import requests
import re
from flask import Flask, request, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from textblob import TextBlob

app = flask.Flask(__name__, template_folder='templates')
model = pickle.load(open('./static/pickle/model.pkl','rb'))

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        user_input_tweet = [request.form["user_input_tweet"]]
        input_text = "'" + request.form["user_input_tweet"] + "' " 
        
        #change to lower case
        clean = request.form["user_input_tweet"].lower()
        # remove punctuation and urls
        clean = re.sub(r"[^\w\d'\s]",'',clean)
        #remove numbers
        clean = re.sub(r"\d+",'',clean)
        # tokenize the text by splitting (leaving apostrophe to be used in remove stop words)
        clean = clean.split()
        #remove stop words
        add = ["i'm", "i've","airlines","airline","flight","united","amp","u","im","ua","pm"]
        to_remove = (stopwords.words("english")) + add
        no_stop=[]
        for i in clean:
            if i not in to_remove:
                no_stop.append(i)
                clean = no_stop
        #join words to one string
        clean = ' '.join(clean)
        #remove apostrophes
        clean = clean.replace("'",'')
        
        # defining and appplying sentiment analysis model (VADER)
        analyser = SentimentIntensityAnalyzer()
        vader_score = "Vader Compound Score : "+ str(analyser.polarity_scores(request.form["user_input_tweet"])['compound'])
        
        #TextBlob
        textblob = "Text Blob Polarity: " + str(TextBlob(clean).sentiment[0])
        
        #predicting the tweet category
        prediction = np.array2string(model.predict([clean]))
        prediction = prediction.replace("[' ","")
        prediction = "classified as: " + prediction.replace("']","") + "    "
        
        return render_template('index.html', input_text=input_text,prediction_text=prediction,vader_score=vader_score,textblob=textblob)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)