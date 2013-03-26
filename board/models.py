from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=32, null=True, blank=True)

class Board(models.Model):
	name = models.CharField(max_length=32, null=True, blank=True)
	category = models.ForeignKey(Category)

class Article(models.Model):
	user = models.ForeignKey(User)
	board = models.ForeignKey(Board)

	title = models.CharField(max_length=100, null=True, blank=True)
	body = models.TextField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now=True, null=False)