"""
test version
Brand Advertising
"""
from urllib.request import urlopen
import tweepy, re, json


# user credentials 
# cate.wl.zhang@gmail.com
# Consumer Key (API Key)	dkm5NZhXmtyLdrif8PCcmIBkX
# Consumer Secret (API Secret)	wOivaCX3qE0XFFuKEbK1aEwLtccrTlIKVTFUeoPpaUnNbCt4Gz

# Access Token	799354686662787072-XDzKnFhMZzAfdPnUKU2JGHE2DW5zgvk
# Access Token Secret	oRhBN2cuZ03Zqxz5lf50uAWRE1TxnRjZEJybXcD1nZYay

consumer_key= "dkm5NZhXmtyLdrif8PCcmIBkX"
consumer_secret= "wOivaCX3qE0XFFuKEbK1aEwLtccrTlIKVTFUeoPpaUnNbCt4Gz"
access_token= "799354686662787072-XDzKnFhMZzAfdPnUKU2JGHE2DW5zgvk"
access_token_secret= "oRhBN2cuZ03Zqxz5lf50uAWRE1TxnRjZEJybXcD1nZYay"


# authotication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

twe_id = '799612084593954817'
us_name = 'jimmyfallon'
print('tweet id:', twe_id)
print('user name:', us_name)

# 'who liked the tweets'
# not exposed in the API
# workaround 
def get_uid_tweet_like(tweet_id):
    try:
        data = urlopen('https://twitter.com/i/activity/favorited_popup?id=' + tweet_id)  # file like obj -> byte
        html = data.read().decode("utf-8")  # string
        data.close()
        ids = re.findall(r'data-user-id=\\"+\d+', html)
        uni_ids = list(set([re.findall(r'\d+', match)[0] for match in ids]))        
        print('who liked the tweets', uni_ids) 
    except Exception as e:
        print(e)
        
get_uid_tweet_like(twe_id)


# 'who retweeted the tweet'
def get_uid_tweet_retweet(tweet_id):
    retweets = []
    retweet_user_ids = []
    try:
        retweets = api.retweets(tweet_id)
        retweet_user_ids = [str(rts._json['user']['id']) for rts in retweets]
        print('who retweeted the tweet', retweet_user_ids)
    except Exception as e:
        print(e)
        
get_uid_tweet_retweet(twe_id)


# 'who made a comment on the tweet' 
# get reply 
max_tweets=1000
def get_uid_reply(user_name, tweet_id):
    query = 'to:'+user_name
    try:
        searched_tweets = [status._json for status in tweepy.Cursor(api.search, q=query, sinceId = int(tweet_id)).items(max_tweets)]
        reply_user_ids = [s['user']['id_str'] for s in searched_tweets if s['in_reply_to_status_id_str']==tweet_id]
        print('who replied the tweet', reply_user_ids)
    except Exception as e:
        print(e)
        
        
get_uid_reply(us_name, twe_id)
