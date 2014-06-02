from django.db import models
from django.contrib.auth.models import User

from board.models import Board

class Article(models.Model):
    user = models.ForeignKey(User)
    board = models.ForeignKey(Board)
    pk_in_board = models.IntegerField(null=False, default=0)

    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True, null=False)
    modified_at = models.DateTimeField(null=True)

    hits = models.IntegerField(null=False, default=0)
    
    ARTICLE_STATUS = (
        ('N', 'Normal'),
        ('L', 'Locked'),
        ('D', 'Deleted'),
        ('S', 'Secret'),
    )
    status = models.CharField(max_length=1, choices=ARTICLE_STATUS, default='N')
    is_notice = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return u'%s - %s' % (self.user.last_name, self.title)

    def change_status(self, s):
        self.status = s
        self.save()
    
    def set_notice(self):
        self.is_notice = True
        self.save()

