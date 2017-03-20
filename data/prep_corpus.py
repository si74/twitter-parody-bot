import twitter
import os
import re

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token_key = os.environ['access_token_key']
access_token_secret = os.environ['access_token_secret']
username = os.environ['username']

api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

print(api.VerifyCredentials())

#Note - we are filtering out retweets and and replies when grabbing the corpus of tweets
statuses = api.GetUserTimeline(screen_name=username,include_rts=False,exclude_replies=True,count=200)

#add to text file
count = 0
with open("data/output.txt", "w") as f:
    for s in statuses:
    #filter out urls in text file
        count = count + 1
        print count
        result = re.sub(r"https\S+", "", s.text)
        result = result + "\n"
        print result
        f.write(result.encode('utf8'))

print "Finished grabbing tweets"
