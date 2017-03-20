import markovify
import time
import twitter
import os

class TwitterBot(object):
    def __init__(self, consumer_key, consumer_secret,access_token_key, access_token_secret, text):
        # initialize twitter Api object
        self.api = twitter.Api(consumer_key=consumer_key,
                              consumer_secret=consumer_secret,
                              access_token_key=access_token_key,
                              access_token_secret=access_token_secret)
        # initialize markov model
        self.model = text_model = markovify.NewlineText(text)

    def tweet(self, interval):
        while(True):
            sentence = self.model.make_short_sentence(140)
            print sentence
            try:
                self.api.PostUpdate(sentence)
            except Exception as inst:
                print inst # catch most exceptions but continue
                continue
            time.sleep(interval)

if __name__ == "__main__":
    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    access_token_key = os.environ['access_token_key']
    access_token_secret = os.environ['access_token_secret']

    print consumer_key
    print consumer_secret
    print access_token_key
    print access_token_secret

    # Get raw text as string.
    with open("data/output.txt") as f:
        text = f.read()

    # initialize twitterBot
    bot = TwitterBot(consumer_key, consumer_secret, access_token_key, access_token_secret, text)

    print "starting..."
    try:
        bot.tweet(300) #bot currently tweets every 5 seconds
    except KeyboardInterrupt:
        print "stopping parody bot"
