import tweepy
import csv
import numpy as np
import textblob
import dotenv
import os


consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

stock = input("Stock: ")

def search(s):
	pos = 0
	neg = 0
	stock_tweets = api.search("$"+s)
	for tweet in stock_tweets:
		analysis = textblob.TextBlob(tweet.text)
		if analysis.sentiment.polarity > 0:
			pos+=1
		else:
			neg+=1

	if pos>neg:
		get_data(stock +'.csv')
		predicted_price
	elif pos<neg:
		return "negative sentiment"
	else:
		return "error."

	return "Stock: %" % s+"\n"+analysis.sentiment