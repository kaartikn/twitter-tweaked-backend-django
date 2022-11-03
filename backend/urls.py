"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authURL', views.getAuthURL),
    path('auth', views.storeCredentials),
    path('tweets', views.tweet),
    path('tweets/search', views.searchTweets),
    path('user/favourite', views.favouriteUser),
    path('tweets/favourite', views.favouriteTweet),
    path('tweets/unfavourite', views.unfavouriteTweet),
    path('tweets/retweet', views.retweetTweet),
    path('tweets/unretweet', views.unretweetTweet),
    path('following', views.getFollowingIds),
    path('users', views.getUserFromUserId),
    path('tweets/top/user', views.getTopTweetsFromUser)
]
