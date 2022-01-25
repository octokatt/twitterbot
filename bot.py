import sys
from os import environ

import tweepy
import quoter

# Pull authentication keys
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

# Set interval for Twitter Bot
INTERVAL = 60 * 60 * 24

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