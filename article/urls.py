from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                        url(r'^(?P<article_id>\d+)/delete/$', 'article.views.article_delete_ok'),
                        url(r'^(?P<article_id>\d+)/$', 'article.views.article_view'),
                        url(r'^write/(?P<board_name>\S+)/ok/$', 'article.views.article_write_ok'),
                        url(r'^write/(?P<board_name>\S+)/$', 'article.views.article_write'),
)
