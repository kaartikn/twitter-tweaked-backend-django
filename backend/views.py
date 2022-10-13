import os
import jsons
from django.http import HttpResponseRedirect
import tweepy
from backend.auth.credentialsVerifier import verifyAccessToken
from backend.twitter_scrape.scrape import queryBuilder, advancedSearch

from backend.auth.oauth1handler import getOAuth1UserHandlerUnauthorized, getOauth1UserHandlerAuthorized
from backend.misc.misc import formatResponse, getRequestBody, getRequestHeaderAccessToken, getRequestHeaderAccessTokenSecret
from .models import Auth, Payload
from .serializers import PayloadSerializer, UserFavouriteAccountsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

@api_view(['POST'])
def getAuthURL(request: Request):
    if request.method == 'POST':
        oauth = getOAuth1UserHandlerUnauthorized()
        authURL = oauth.get_authorization_url()

        # request_token = oauth.request_token["oauth_token"]
        # request_secret = oauth.request_token["oauth_token_secret"]

        # auth = Auth(request_token, request_secret)
        # auth.save()

        serializer = PayloadSerializer(formatResponse(authURL, status.HTTP_200_OK))
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def storeCredentials(request: Request):
    # oauth_token = request.GET.get('oauth_token')
    # oauth_verifier = request.GET.get('oauth_verifier')
    # auth = Auth.objects.get(request_token=oauth_token)
    # oauth = getOAuth1UserHandlerUnauthorized()
    # oauth.request_token = {
    #     "oauth_token": auth.request_token,
    #     "oauth_token_secret": auth.request_secret
    # }

    if request.method == 'POST':
        req_body = getRequestBody(request)
        auth = Auth(req_body["twitter_session_id"], req_body["oauth_token"], req_body["oauth_verifier"])
        auth.save()

        return Response(status=status.HTTP_204_NO_CONTENT) 


    # access_token, access_token_secret = oauth.get_access_token(oauth_verifier)
    # print("Access Token is  " + access_token)
    # print("Access Token Secret is  " +access_token_secret)
    # return HttpResponseRedirect("https://www.twitter.com")

@api_view(['POST'])
def tweet(request: Request):
    access_token = request.headers.get('Access-Token')
    access_token_secret = request.headers.get('Access-Token-Secret')
    verifyAccessToken(access_token)

    #Authentication stuff then tweet stuff

    if request.method == 'POST':
        req_body = getRequestBody(request)
        oauth = getOauth1UserHandlerAuthorized(access_token, access_token_secret)
        api = tweepy.API(oauth)
        api.update_status(req_body['text'])
        # Look at how to use models to extract API Request Bodies
        
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['POST'])
def searchTweets(request: Request):
    access_token = getRequestHeaderAccessToken(request)
    access_token_secret = getRequestHeaderAccessTokenSecret(request)
    verifyAccessToken(access_token)

    if request.method == 'POST':
        content = getRequestBody(request)
        query = queryBuilder(content["all_words_query"], content["exact_phrase"], content["any_of_these_words"], content["none_of_these_words"], content["hashtags"], content["from_accounts"], content["to_accounts"], content["mentioning_accounts"], content["min_replies"], content["min_faves"], content["min_retweets"], content["language"], content["to_date"], content["from_date"], content["show_replies"], content["show_replies_only"], content["show_links"], content["show_links_only"])
        tweets = advancedSearch(query, access_token, access_token_secret)
        res = {
            "query": query,
            "tweets": jsons.dumps(tweets)
        }
        return Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def favouriteUser(request: Request):
    access_token = getRequestHeaderAccessToken(request)
    verifyAccessToken(access_token)

    # Expects a list of favourite users as request body
    if request.method == 'POST':
        req_body = getRequestBody(request)
        serializer = UserFavouriteAccountsSerializer(data=req_body, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def favouriteTweet(request: Request):
    access_token = request.headers.get('Access-Token')
    access_token_secret = request.headers.get('Access-Token-Secret')
    verifyAccessToken(access_token)

    # Expects a list of favourite users as request body
    if request.method == 'POST':
        req_body = getRequestBody(request)
        oauth = getOauth1UserHandlerAuthorized(access_token, access_token_secret)
        api = tweepy.API(oauth)
        api.create_favorite(req_body['id'])
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def unfavouriteTweet(request: Request):
    access_token = request.headers.get('Access-Token')
    access_token_secret = request.headers.get('Access-Token-Secret')
    verifyAccessToken(access_token)

    # Expects a list of favourite users as request body
    if request.method == 'POST':
        req_body = getRequestBody(request)
        oauth = getOauth1UserHandlerAuthorized(access_token, access_token_secret)
        api = tweepy.API(oauth)
        api.destroy_favorite(req_body['id'])
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def retweetTweet(request: Request):
    access_token = request.headers.get('Access-Token')
    access_token_secret = request.headers.get('Access-Token-Secret')
    verifyAccessToken(access_token)

    # Expects a list of favourite users as request body
    if request.method == 'POST':
        req_body = getRequestBody(request)
        oauth = getOauth1UserHandlerAuthorized(access_token, access_token_secret)
        api = tweepy.API(oauth)
        api.retweet(req_body['id'])
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def unretweetTweet(request: Request):
    access_token = request.headers.get('Access-Token')
    access_token_secret = request.headers.get('Access-Token-Secret')
    verifyAccessToken(access_token)

    # Expects a list of favourite users as request body
    if request.method == 'POST':
        req_body = getRequestBody(request)
        oauth = getOauth1UserHandlerAuthorized(access_token, access_token_secret)
        api = tweepy.API(oauth)
        api.unretweet(req_body['id'])
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getPublicFollowing(request: Request):
    access_token = request.headers.get('Access-Token')
    access_token_secret = request.headers.get('Access-Token-Secret')
    verifyAccessToken(access_token)

    if request.method == 'GET':
        oauth = getOauth1UserHandlerAuthorized(access_token, access_token_secret)
        api = tweepy.API(oauth)
        following = api.get_friends()
        print(following[0])
        return Response(following[0]._json, status=status.HTTP_200_OK)






















# @api_view(['GET', 'PUT', 'DELETE'])
# def auth_detail(request: Request, id: int):

#     try:
#         auth = Auth.objects.get(pk=id)
#     except Auth.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'GET':
#         serializer = AuthSerializer(auth)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = AuthSerializer(auth, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         auth.delete()
#         return Response(status=status.HTTP_204_NO_req_body)