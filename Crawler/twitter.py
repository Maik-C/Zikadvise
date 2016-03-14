import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from sys import argv

script, hashtag = argv

consumer_key = 'AHeecbv2tqY3YJoWMHVBbuV1t'
consumer_secret = 'sqNqbgiNh7AA7auH9Q1aru7HLnVavgmfevkervMJ20Z3hfTcsW'
access_token = '4875812823-C4yK1NcnlsoOyNJBowWi08a6L01BO75cuEuOzJz'
access_secret = 'Cw8VkrbLnJmPejE6T4tYcTSTIqrBw5NgDpysoaXKYeJ4j'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open(hashtag+'.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#'+hashtag])