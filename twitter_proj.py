#!/usr/bin/env python
import twitter_cred
import sys
import tweepy
from wordcloud import WordCloud
from PIL import Image


def listToString(s):
    # initialize an empty string
    str1 = ""

    for ele in s:
        str1 += ele + ' '

    return str1

auth = tweepy.OAuthHandler(twitter_cred.API_KEY, twitter_cred.API_SECRET)
auth.set_access_token(twitter_cred.ACCESS_TOKEN, twitter_cred.ACCESS_SECRET)

api = tweepy.API(auth)

keyword = sys.argv[1]

tweetslst = []

for tweet in api.search(q = keyword, lang = 'en', result_type = 'popular', tweet_mode = 'extended', count = 20):
    tweet.full_text = tweet.full_text.encode('unicode-escape').decode('utf-8')
    tweetlist = tweet.full_text.split(' ')
    tweetslst = tweetslst + tweetlist


res = [x for x in tweetslst if not x.startswith('https')]



strvar = listToString(res)



strvarlow = strvar.lower()

wc = WordCloud(max_font_size=100, width=600, height=300, relative_scaling=.5)

wc.generate(strvarlow)

wc.to_file('output.png')


img = Image.open('output.png')
img.show()








