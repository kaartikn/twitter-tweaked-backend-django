import json

def formatResponse(payload, responseStatus: int = 200):
    return {'payload': payload, 'responseStatus': responseStatus}

def formatResponseTweetJSON(tweetUrl, date, content, renderedContent, replyCount, retweetCount, likeCount, quoteCount, media, quotedTweet, username, displayName, verified, profileImageUrl, profileUrl):
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
    "username": username,
    "displayName": displayName,
    "verified": verified,
    "profileImageUrl": profileImageUrl,
    "profileUrl": profileUrl,
    }
    return response

