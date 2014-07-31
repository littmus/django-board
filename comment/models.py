from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from article.models import Article


class Comment(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)

    body = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __unicode__(self):
        return u'%s - %s' % (self.user.last_name, self.body[:20])

    def get_absolute_url(self):
        return reverse('article', args=(self.article.pk, ))

