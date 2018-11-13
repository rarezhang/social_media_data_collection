'''
 associated with my own twitter account

oauth.consumerKey=7lIJF60LOeqEjr21r1FYg
oauth.consumerSecret=Mr0NAcBsHFSsoMVy33TgnFebpilocEWolMaVkzNs
oauth.accessToken=342531857-kXfBgfU7bRkFwnBPxzDbnvFYPK6sCMxT2pP0WN6r
oauth.accessTokenSecret=7UFrjilryikG1nWPcKxjxidHvW6rB0xngvADRc5zgm4
'''

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import datetime

# user credentials
access_token = "2788136796-IRvS3V3ZRAZx8gRE1OBzUpADXfQiGUaMIYrWyNQ"
access_token_secret = "GU4duYToRWhWnfWYgkYbz5CPy73XT0PoWeS24XbZGgQXd"
consumer_key = "u5DkUHFYiHFgjthvcivFKb1r9"
consumer_secret = "2Gxi8Ng6bI13ZWbCoyflXJlBkyb0S08Y0HTRjk9Mn98A7JTPdp"


fname = '..//data//asthma_'
path_out_put = fname + str(datetime.datetime.now().strftime("%Y_%m_%d"))
keywords = ["asthma","asthma attack","inhaler","wheezing","sneezing","runny nose","Albuterol","Xolair","Montelukast","Nebulizer","Flovent","Singulair","Advair","Bronchodilator","Bronchodilators","short of breath","chest tight","difficulty breathing","trouble breathing"]

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