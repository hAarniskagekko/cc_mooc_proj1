from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from random import randrange
from .forms import TweetPwForm
from .models import Tweet

@login_required(login_url='login/')
def index(request):
	return render(request, 'cc_mooc_proj1/index.html')

@login_required(login_url='login/')
def tweet_passwd(request):
	tweets10 = Tweet.objects.all().order_by('-id')[:10]
	form = TweetPwForm()
	return render(request, 'cc_mooc_proj1/tweet_pw.html', {'tweets10' : tweets10, 'form' : form})

@login_required(login_url='login/')
def post_tweet(request):
	form = TweetPwForm(request.POST)
	form.is_valid()

	tweet = Tweet(content=form.cleaned_data['tweet_content'])
	tweet.save()

	form = TweetPwForm()
	return redirect('tweet_passwd')

def secret_of_the_day(request):
	idioms = ["Fish spawn in quiet waters", "It's more fun to look into the mouth of a laughing one than a crying one", "Rakes and pitchforks are peasants tools; books and cards area badges of bliss"]
	rand_number = randrange(3)
	select_idiom = idioms[rand_number]

	return render(request, 'cc_mooc_proj1/secret_of_the_day.html', {'idiom' : select_idiom})
