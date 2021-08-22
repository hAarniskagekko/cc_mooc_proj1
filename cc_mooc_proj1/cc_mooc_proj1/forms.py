from django import forms

class TweetPwForm(forms.Form):
	tweet_content = forms.CharField(label='Your password:', max_length=100)