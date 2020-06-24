import tweepy
import numpy as np
import textblob
import json
import urllib.request

consumer_key = 'QAA5a07Q5zDDLiU9jStIJ2bOR'
consumer_secret = 'VuLAZs6AtKnJKF67JvqGRWAgqMyqUPO8ezEJyhKaqWnSddM7RA'
access_token = '1103708820495306752-7Zm9dYrITLoyWhFXsxeNajO8hQOjGY'
access_token_secret = 'tpwsT3YZH8MsSutXNOPHmYgeUMTomqnYhuJhEHxtnADSe'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
data = ''
QUERY_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=API_KEY&symbol="
API_KEY = 'P8OMFY0KV1G7EUKF'

class Stocks():
    def __init__(self):
        self.tweetStrings = ""
        self.polList = []
    
    def printResults(self, data):
        try:
            theJSON = json.loads(data)
            print(theJSON['Meta Data']['2. Symbol'])
            date = theJSON['Meta Data']['3. Last Refreshed']
            print(date)
            result = theJSON['Time Series (Daily)'][date]
            return(result)
        except:
            print("ERROR, stock does not exist")
            
    def get_daily_data(self, symbol):
        url = QUERY_URL+symbol
        webUrl = urllib.request.urlopen(url)
        data = webUrl.read()
        return self.printResults(data)
        
    def search(self, stockTicker):
        query = "$" + stockTicker
        tweetCount = 500
        response = ""
        stock_tweets = api.search(q=query, count=tweetCount)
        polSum = sum(self.polList)
        polString = ""
        polAvg = 0
        try:
            for tweet in stock_tweets:
                analysis = textblob.TextBlob(tweet.text)
                pol = analysis.sentiment.polarity
                self.tweetStrings+= str(textblob.TextBlob(tweet.text) + "\n")
                self.polList.append(pol)
                if(pol>0):
                    polAvg = polAvg + 1
                if(pol<0):
                    polAvg = polAvg - 1
                if(pol==0):
                    polAvg = polAvg
            if(polAvg > 0):
                polString = " POSITIVE "
            if (polAvg < 0):
                polString = " NEGATIVE "
            else:
                polString = " NEUTRAL "
            response = "Polarity: " + str(polAvg) + "\n Analysis: " + polString + " (out of %s tweets): " %tweetCount
            return response
        except:
            print("Error With Twitter Search Results")
            
