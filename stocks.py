import tweepy
import csv
import numpy as np
import textblob

consumer_key = 'XXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXX'
access_token = 'XXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXX'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class Stocks():

	def __init__(self):
		self.tweetStrings = ""
		self.polList = []

	def search(self, stockTicker):
		query = "$" + stockTicker
		tweetCount = 500
		response = ""
		stock_tweets = api.search(q=query, count=tweetCount)
		polSum = sum(self.polList)
		polString = ""
		polAvg = 0
		
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
			
		if (polAvg > 0):
		    polString = " POSITIVE "
		if (polAvg < 0):
		    polString = " NEGATIVE "
		if (polAvg == 0):
		    polString = " NEUTRAL "
			    
		response = "Polarity: " + str(polAvg) + "\n Analysis: " + polString + " (out of %s tweets): " %tweetCount
		return response