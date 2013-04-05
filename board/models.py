from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=32, null=True, blank=True)

	def __unicode__(self):
		return self.name

class Board(models.Model):
	name = models.CharField(max_length=32, null=True, blank=True)
	category = models.ForeignKey(Category)

	def __unicode__(self):
		return u'%s - %s' % (self.category.name, self.name)