from django.db import models

class Tweet(models.Model):
	content = models.CharField(max_length=100)