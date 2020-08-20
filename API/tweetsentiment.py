import tweepy as tp
from textblob import TextBlob

consumerKey = "bQJAEnxonwym2SAdVvI5b15oF"
consumerSecret = "efEMCNLhCQD1YuMIxCUmu2wO932ya3mnN03EcBCSOIwqVkkoku"

accessToken = "2418673364-aGDMYDHjeWjlKWcIqGSVTHar8vigCJcGCbEHcwQ"
accessTokenSecret = "ZwZlFd7Fry1rjqGkK7aLkbFXB4hTQ0xFeIiGQlVwGZL5T"

auth = tp.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tp.API(auth)

publicTweets = api.search("weehee")

for tweet in publicTweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
