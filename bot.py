import markovify
from time import sleep
import twitter

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token_key = os.environ['access_token_key']
access_token_secret = os.environ['access_token_secret']
username = os.environ['username']

api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

# Get raw text as string.
with open("output.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

#Bot tweeting every five minutes
def tweet_something(name):
    sentence = text_model.make_short_sentence(140)
    api.PostUpdate(sentence)

print "starting..."
rt = RepeatedTimer(1, hello, "World") # it auto-starts, no need of rt.start()
try:
    sleep(300) #
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!
