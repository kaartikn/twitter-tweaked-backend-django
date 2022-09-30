from rest_framework.request import Request
import json

def formatResponse(payload, responseStatus: int = 200):
    return {'payload': payload, 'response_status': responseStatus}

def formatResponseTweetJSON(tweetUrl, date, content, renderedContent, replyCount, retweetCount, likeCount, quoteCount, media, quotedTweet, id, mentionedUsers, hashtags, favorited, retweeted, username, displayName, verified, profileImageUrl, profileUrl):
    response = {
    "tweetUrl": tweetUrl,
    "date": date,
    "content": content,
    "renderedContent": renderedContent,
    "replyCount": replyCount,
    "retweetCount": retweetCount,
    "likeCount": likeCount,
    "quoteCount": quoteCount,
    "media": media,
    "quotedTweet": quotedTweet,
    "id": id, 
    "mentionedUsers": mentionedUsers, 
    "hashtags": hashtags,
    "favorited": favorited,
    "retweeted": retweeted,
    "username": username,
    "displayName": displayName,
    "verified": verified,
    "profileImageUrl": profileImageUrl,
    "profileUrl": profileUrl,
    }
    return response

def getRequestBody(request: Request):
    return json.loads(request.body.decode('utf-8'))

def getRequestHeaderAccessToken(request: Request):
    return request.headers.get('Access-Token')

def getRequestHeaderAccessTokenSecret(request: Request):
    return request.headers.get('Access-Token-Secret')