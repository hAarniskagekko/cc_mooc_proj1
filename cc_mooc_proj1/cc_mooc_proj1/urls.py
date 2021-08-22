from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('tweet_passwd/', views.tweet_passwd, name='tweet_passwd'),
    path('post_tweet/', views.post_tweet, name='post_tweet'),
]
