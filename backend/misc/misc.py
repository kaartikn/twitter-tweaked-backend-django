from rest_framework.request import Request
import json

def formatResponse(payload, responseStatus: int = 200):
    return {'payload': payload, 'responseStatus': responseStatus}

def getRequestBody(request: Request):
    return json.loads(request.body.decode('utf-8'))

def getRequestHeaderAccessToken(request: Request):
    return request.headers.get('Access-Token')