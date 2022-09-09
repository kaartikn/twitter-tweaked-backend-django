from dataclasses import fields
from rest_framework import serializers
from .models import Auth, Payload

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ['request_token', 'request_secret']

class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = ['payload', 'responseStatus']