from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Questions(models.Model):
	question = models.CharField(max_length=250)
	option1 = models.CharField(max_length=128)
	option2 = models.CharField(max_length=128)
	option3 = models.CharField(max_length=128)
	option4 = models.CharField(max_length=128)
	correct_ans = models.CharField(max_length=128)
        is_valid = models.BooleanField(default=False)

	def __unicode__(self):
		return self.question

class person(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	play = models.ForeignKey(Questions)
	def __unicode__(self):
		return self.user.username

