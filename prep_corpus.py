import twitter
import os

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

statuses = api.GetUserTimeline(screen_name=username,include_rts="False",count=200)

print([s.text for s in statuses])

#add to text file
with open("output.txt", "w") as f:
	for s in statuses:
		f.write(s.text.encode('utf8'))
