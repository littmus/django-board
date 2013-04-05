from django.db import models
from django.contrib.auth.models import User

from board.models import Board

class Article(models.Model):
	user = models.ForeignKey(User)
	board = models.ForeignKey(Board)

	title = models.CharField(max_length=100, null=True, blank=True)
	body = models.TextField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now=True, null=False)

	hits = models.IntegerField(null=False, default=0)

	def __unicode__(self):
		return u'%s - %s' % (self.user.last_name, self.title)