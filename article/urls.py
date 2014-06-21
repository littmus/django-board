from django.conf.urls import patterns, url
from article.views import ArticleView, ArticleWriteView, ArticleEditView


"""
urlpatterns = patterns('',
                        url(r'^(?P<article_id>\d+)/edit/$', 'article.views.article_edit'),
                        url(r'^(?P<article_id>\d+)/edit_ok/$', 'article.views.article_edit_ok'),
                        url(r'^(?P<article_id>\d+)/delete/$', 'article.views.article_delete_ok'),
                        url(r'^(?P<article_id>\d+)/$', 'article.views.article_view'),
                        url(r'^write/(?P<board_id>\d+)/ok/$', 'article.views.article_write_ok'),
                        url(r'^write/(?P<board_id>\d+)/$', 'article.views.article_write'),
)
"""

urlpatterns = patterns('',
    url(r'^(?P<article_pk>\d+)/edit/$', ArticleEditView.as_view()),
    url(r'^(?P<article_pk>\d+)/$', ArticleView.as_view(), name='article'),
    url(r'^write/(?P<board_pk>\d+)/$', ArticleWriteView.as_view()),
)
