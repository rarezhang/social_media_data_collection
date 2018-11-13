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
access_token = "342531857-kXfBgfU7bRkFwnBPxzDbnvFYPK6sCMxT2pP0WN6r"
access_token_secret = "7UFrjilryikG1nWPcKxjxidHvW6rB0xngvADRc5zgm4"
consumer_key = "7lIJF60LOeqEjr21r1FYg"
consumer_secret = "Mr0NAcBsHFSsoMVy33TgnFebpilocEWolMaVkzNs"


fname = '..//data//vector_'
path_out_put = fname + str(datetime.datetime.now().strftime("%Y_%m_%d"))
keywords = ["abdominal pain", "activity change", "acute kidney injury", "altered mental status", "appetite change", "arthralgia", "arthralgias", "back ache", "back pain", "blurred vision", "blurry vision", "body ache", "body aches", "bone pain", "chills", "clammy", "constant throbbing headache", "cough", "coughing", "decreased activity", "decreased appetite", "decreased awareness", "diaphoresis", "diarrhea", "diffuse rash", "dizziness", "elevated lft", "fatigue", "fever", "flaccid paralysis", "headache", "hematuria", "hemoconcentration", "high grade fever", "increased agitation", "increasing obtundation", "joint pain", "joint swelling", "lack of appetite", "lethargic", "leukopenia", "loss of appetite", "lymphadenopathy", "macular rash on upper body", "menses longer than usual.", "mild nausea", "mild sore throat", "muscle aches", "muscle pain", "muscle weakness", "myalgia", "n/v/d", "nausea", "nausea diarrhea", "neck pain", "neck stiffness", "numbness in hands", "pain in knees", "pain in wrists", "petechiae", "petechial on lower body", "photophobia", "rash", "red eyes", "rigors", "seizure", "severe headache", "somnolence", "sore throat", "stiffness", "swollen feet hands", "throbbing", "thrombocytopenia", "thrombocytopenic", "tiny nose bleed", "transaminitis", "tremors", "unable to focus eyes", "unable to walk ", "unconscious", "vomiting", "weakness", "wide based gait", "worsening gait"]

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