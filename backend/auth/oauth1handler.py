import tweepy

from django.conf import settings

consumer_key = "mQGB54CXLKG12UqcPyKDvU97c"
consumer_secret = "tKOcKKkUQMoAsTIS1irEVC2VBByvJV8YqVX2cbJ19Ds6yilD9f"

def getOAuth1UserHandlerUnauthorized() -> tweepy.OAuth1UserHandler :

    oauth1_user_handler = tweepy.OAuth1UserHandler(
        consumer_key=consumer_key, 
        consumer_secret=consumer_secret, 
        callback='https://www.twitter.com/home'
        )

    return oauth1_user_handler

def getOauth1UserHandlerAuthorized(access_token: str, access_token_secret) -> tweepy.OAuth1UserHandler :
    oauth1_user_handler = tweepy.OAuth1UserHandler(
        consumer_key, 
        consumer_secret, 
        access_token, 
        access_token_secret
    )
    return oauth1_user_handler

