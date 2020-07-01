import twitter_cred
import tweepy
#from tweepy import OAuthHandler

auth = tweepy.OAuthHandler(twitter_cred.API_KEY, twitter_cred.API_SECRET)
auth.set_access_token(twitter_cred.ACCESS_TOKEN, twitter_cred.ACCESS_SECRET)

api = tweepy.API(auth)

keyword = "trump"

tweetslst = []

for tweet in api.search(q = keyword, lang = 'en', result_type = 'popular', tweet_mode = 'extended', count = 20):
    tweet.full_text = tweet.full_text.encode('unicode-escape').decode('utf-8')
    tweetlist = tweet.full_text.split(' ')
    tweetslst = tweetslst + tweetlist

tweetslst.sort()
final_list = list()
print(len(tweetslst))
for word in tweetslst:
    if word not in final_list:
        final_list.append(word)

# flat_list = []
# for sublist in final_list:
#     for word in sublist:
#         flat_list.append(word)


res = [x for x in final_list if not x.startswith('https')]
# res = []
# flag = 1
# char_list = ('https')
# for ele in final_list:
#     for idx in char_list:
#         if idx not in ele:
#             flag = 1
#         else:
#             flag = 0
#             break
#     if(flag == 1):
#         res.append(ele)
res.sort()
print(len(res))
print(res)







