# twitter-parody-bot
A few scripts using Markov Chains to make a parody twitter account

## Background

## Grab Relevant Twitter Tokens

Head to [apps.twitter.com](http://apps.twitter.com):

Create an application (should create consumer key and secret):

Generate access tokens for the given application:

Initialize a configuration script:

```
vim config.sh
```

and substitute in your values:

```
export consumer_key="MY_CONSUMER_KEY"
export consumer_secret="MY_CONSUMER_SECRET"
export access_token_key="MY_ACCESS_TOKEN_KEY"
export access_token_secret="MY_ACCESS_TOKEN_SECRET"
export username="PARODY_USERNAME"
```

## Setup

```
pip install python-twitter
pip install markovify
```

Run `python prep_corpus.py` to generate a sample of twitter statuses for the username
you wish to parody.

Run `bot.py` which will run a bot forever that will post a status every 5 minutes.

## Wercker Pipeline
