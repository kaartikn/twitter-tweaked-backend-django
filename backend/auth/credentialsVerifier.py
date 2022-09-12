from http.client import HTTPResponse

def verifyAccessToken(accessToken: str):
    # Refactor for DB to store accessToken and check accordingly
    if accessToken == "":
        return HTTPResponse("User is unverified", status=401)
