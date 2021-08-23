from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweetPwForm
from .models import Tweet

@login_required(login_url='login/')
def index(request):
	return render(request, 'cc_mooc_proj1/index.html')

def tweet_passwd(request):
	tweets10 = Tweet.objects.all().order_by('-id')[:10]
	form = TweetPwForm()
	return render(request, 'cc_mooc_proj1/tweet_pw.html', {'tweets10' : tweets10, 'form' : form})

def post_tweet(request):
	form = TweetPwForm(request.POST)
	form.is_valid()

	tweet = Tweet(content=form.cleaned_data['tweet_content'])
	tweet.save()

	form = TweetPwForm()
	return redirect('tweet_passwd')
