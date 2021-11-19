import tweepy
import credentials as cred
import quoter


# Authenticate to Twitter
auth = tweepy.OAuthHandler(cred.CONSUMER_KEY, cred.CONSUMER_SECRET)
auth.set_access_token(cred.ACCESS_TOKEN, cred.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet
tweet = quoter.assemble()
api.update_status(tweet)

