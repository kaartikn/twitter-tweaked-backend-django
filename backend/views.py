import json
import os
from django.http import HttpResponseRedirect
import tweepy

from backend.auth.oauth1handler import getOAuth1UserHandlerUnauthorized, getOauth1UserHandlerAuthorized
from backend.misc.misc import formatResponse
from .models import Auth, Payload
from .serializers import AuthSerializer, PayloadSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

@api_view(['GET'])
def getAuthURL(request: Request):
    if request.method == 'GET':
        oauth = getOAuth1UserHandlerUnauthorized()
        authURL = oauth.get_authorization_url()

        request_token = oauth.request_token["oauth_token"]
        request_secret = oauth.request_token["oauth_token_secret"]


        auth = Auth(request_token, request_secret)
        auth.save()

        serializer = PayloadSerializer(formatResponse(authURL))

        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def processCallbackAuth(request: Request):
    if request.GET.get('denied'):
        serializer = PayloadSerializer(formatResponse("Access Denied", status.HTTP_401_UNAUTHORIZED))
        return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)
    else:
        oauth_token = request.GET.get('oauth_token')
        oauth_verifier = request.GET.get('oauth_verifier')
        auth = Auth.objects.get(request_token=oauth_token)
        oauth = getOAuth1UserHandlerUnauthorized()
        oauth.request_token = {
            "oauth_token": auth.request_token,
            "oauth_token_secret": auth.request_secret
        }

        access_token, access_token_secret = oauth.get_access_token(oauth_verifier)
        print("Access Token is  " + access_token)
        print("Access Token Secret is  " +access_token_secret)
        return HttpResponseRedirect("https://www.twitter.com")

@api_view(['POST'])
def tweet(request: Request):

    access_token = request.headers.get('Access-Token')
    access_token_secret = request.headers.get('Access-Token-Secret')
    print("Credentials below")
    print(access_token)
    print(access_token_secret)
    content = json.loads(request.body.decode('utf-8'))
    oauth = getOauth1UserHandlerAuthorized(access_token, access_token_secret)
    api = tweepy.API(oauth)
    api.update_status(content['text'])
    
    return Response(status=status.HTTP_204_NO_CONTENT)
























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
#         return Response(status=status.HTTP_204_NO_CONTENT)