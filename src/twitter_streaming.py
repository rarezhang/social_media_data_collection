from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import datetime
from twitter_auth import consumer_key, consumer_secret, access_token, access_token_secret

fname = '..//data//file_name'  # to do 
path_out_put = fname + str(datetime.datetime.now().strftime("%Y_%m_%d"))
keywords = ['keywords']  # to do 


class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        # write the results into file
        with open(path_out_put, 'a') as f:   #a: append
            f.write(data)
            #json.dump(data,f,indent=1)
            return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    # Twitter authetification and the connection to Twitter Streaming API
    listen = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    while True:
        try:
            # filter Twitter Streams to capture data by the keywords.
            stream = Stream(auth, listen)
            stream.filter(track=keywords)
        except KeyboardInterrupt:
            stream.disconnect()
            break
        except:
            continue