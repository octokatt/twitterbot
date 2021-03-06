import sys
from os import environ
import tweepy
import time

import quoter


# Pull authentication keys from environment
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']


# Set interval for Twitter Bot, currently eight hours
INTERVAL = 60 * 60 * 8

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Tweet every Interval
while True:
	print("assembling quote...")
	tweet = quoter.assemble()
	api.update_status(tweet)
	time.sleep(INTERVAL)