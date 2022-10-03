from dataclasses import fields
from rest_framework import serializers
from .models import Auth, Payload, UserFavouriteAccounts

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ['twitter_session_id', 'oauth_token', 'oauth_verifier']

class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = ['payload', 'response_status']

# class AuthenticatedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Authenticated
#         fields = ['access_token', 'email_address', 'account_id']

class UserFavouriteAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavouriteAccounts
        fields = ['account_id', 'favourited_id']