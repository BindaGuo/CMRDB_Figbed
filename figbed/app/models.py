from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

class Figure(models.Model):
	originName = models.CharField(max_length=50)
	newName = models.CharField(max_length=50)
	type = models.CharField(max_length=10)
	created_date = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User)
	def __str__(self):
		return self.originName

class Tag(models.Model):
	name = models.CharField(max_length=50)
	remark = models.CharField(max_length=100)

class FigTag(models.Model):
	figureID = models.ForeignKey(Figure)
	tagID = models.ForeignKey(Tag)
