"""
collect tweets from a single user 

download a user's recent tweets up to a maximum of 3200 the response 
returned in JSON format 
"""

import tweepy, json
from twitter_auth import consumer_key, consumer_secret, access_token, access_token_secret
 

# authotication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def write_file(path, all_tweets):
    """
    dump json write to file 
    """
    with open(path, 'w', encoding='utf-8', errors='ignore') as f:
        for status in all_tweets:
            json.dump(status._json, f, ensure_ascii=False, sort_keys=True, indent=4)

def user_tweets_archive(screen_name):
    """
    @para: screen_name: twitter user screen name 
    """
    all_tweets = []
    # make initial request for most recent tweets (200 is the maximum allowed count)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    
    # id of the last tweet less one
    last = tweets[-1].id - 1
    
    # keep grabbing tweets until there are no tweets left to grab
    while len(tweets) > 0:        
        # all subsiquent requests use the max_id param to prevent duplicates
        tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=last)        
        #save most recent tweets
        all_tweets.extend(tweets)        
        #update the id of the oldest tweet less one        
        last = tweets[-1].id - 1 if len(tweets) > 0 else None
        print(f"{len(all_tweets)} tweets downloaded so far")
        
        
    path = f'..\\data\\{screen_name}.json'
    write_file(path, all_tweets)



if __name__ == '__main__':
    #pass in the username of the account you want to download
    
    screen_name = "@realDonaldTrump"
    user_tweets_archive(screen_name) 
    
    # path = f'..\\data\\{screen_name}.json'
    # with open(path) as f:
        # result = json.load(f, encoding='utf-8')
    # print(result)