
def formatResponse(payload, responseStatus: int = 200):
    return {'payload': payload, 'responseStatus': responseStatus}