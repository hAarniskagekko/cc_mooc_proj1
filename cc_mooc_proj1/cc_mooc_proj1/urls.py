from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='cc_mooc_proj1/login.html')),
    path('', views.index, name='index'),
    path('tweet_passwd/', views.tweet_passwd, name='tweet_passwd'),
    path('post_tweet/', views.post_tweet, name='post_tweet'),
    path('secret_of_the_day/', views.secret_of_the_day, name='secret_of_the_day'),
]
