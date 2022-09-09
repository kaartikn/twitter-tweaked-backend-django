import tweepy

from django.conf import settings

consumer_key = settings.CONSUMERKEY
consumer_secret = settings.CONSUMERSECRET

def getOAuth1UserHandlerUnauthorized() -> tweepy.OAuth1UserHandler :

    oauth1_user_handler = tweepy.OAuth1UserHandler(
        consumer_key=consumer_key, 
        consumer_secret=consumer_secret, 
        callback='http://127.0.0.1:8081/auth/callback'
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

