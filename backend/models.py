from operator import truediv
from django.db import models


class Auth(models.Model):
    request_token = models.CharField(max_length=100, primary_key=True)
    request_secret = models.CharField(max_length=100)

    def __str__(self):
        return self.request_token

class Payload(models.Model):
    payload = models.TextField()
    responseStatus = models.IntegerField()

    class Meta:
        managed = False

class AdvancedSearch():
    all_words_query : str
    exact_phrase : str
    any_of_these_words : list
    none_of_these_words : list
    hashtags: list
    from_accounts: list
    to_accounts: list
    mentioning_accounts: list
    min_replies: int
    min_faves: int
    min_retweets: int
    language: str
    to_date: str
    from_date: str
    show_replies: bool
    show_replies_only: bool
    show_links: bool
    show_links_only: bool