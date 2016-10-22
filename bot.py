import markovify

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token_key = os.environ['access_token_key']
access_token_secret = os.environ['access_token_secret']
username = os.environ['username']

# Get raw text as string.
with open("output.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

#Bot tweeting every five minutes
# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))
