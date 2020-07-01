import twitter_cred
from tweepy import OAuthHandler

auth = OAuthHandler(twitter_cred.API_KEY, twitter_cred.API_SECRET)
auth.set_access_token(twitter_cred.ACCESS_SECRET, twitter_cred.ACCESS_SECRET)



