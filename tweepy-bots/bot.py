# Print tweets in console
import tweepy
import datetime
import json

with open('keys.json') as file:
    data = json.load(file)

consumer_key = data['consumer_key']
consumer_secret = data['consumer_secret']
access_token = data['access_token']
access_token_secret = data['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# Get the User object for twitter...
user = api.get_user('unusual_whales')
# print(json.dumps(user. indent = 4))
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)

for tweet in api.user_timeline('unusual_whales'):
    print(tweet)
    break
