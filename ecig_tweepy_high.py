#!/usr/bin/env python
# coding=utf-8
'''
 586 account
 debug=true
 jsonStoreEnabled=true
 oauth.consumerKey=u5DkUHFYiHFgjthvcivFKb1r9
 oauth.consumerSecret=2Gxi8Ng6bI13ZWbCoyflXJlBkyb0S08Y0HTRjk9Mn98A7JTPdp
 oauth.accessToken=2788136796-IRvS3V3ZRAZx8gRE1OBzUpADXfQiGUaMIYrWyNQ
 oauth.accessTokenSecret=GU4duYToRWhWnfWYgkYbz5CPy73XT0PoWeS24XbZGgQXd
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


fname = '..//data//ecig_high_'
path_out_put = fname + str(datetime.datetime.now().strftime("%Y_%m_%d"))
keywords = ['e-cartridge', 'e-cig', 'e-cigar', 'e-cigaret', 'e-cigarete', 'e-cigarette', 'e-cigarette forum', 'e-cigarettes', 'e-cigarret', 'e-cigarrete', 'e-cigarrette', 'e-cigs', 'e-hookah', 'e-juice','e-liquid', 'e-nicot', 'e-nicotine', 'e-pipe', 'e-vapor', 'ecig', 'ecigs', 'ecigarettes', 'electronic-cig', 'electronic cig', 'electronic-cigarette', 'electronic cigarette', 'electronic cigarettes','electronic vaporizer', 'Joyetech', 'Kanger', 'madvapes', 'personal hookah', 'personal-hookah', 'personal vaporizer', 'personal-vaporizer', 'Provape', 'Provari', 'SmokTech', 'vape', 'vapedaily', 'vapefam', 'vapejuice', 'vapelife', 'vapenation', 'vaper', 'vapers', 'vaping', 'vaping.com', 'www.madvapes.com']

class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        # write the results into file
        with open(path_out_put, 'a') as f:   #a: append
            f.write(data)
            #json.dump(data,f,indent=1)
            return True

    def on_error(self, status):
        print(status)

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


