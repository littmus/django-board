from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
						url(r'^$', 'board.views.board_view'),
						url(r'^article/$', 'board.views.article_view'),
						url(r'^article_write/$', 'board.views.article_write'),
						url(r'^article_write_ok/$', 'board.views.article_write_ok'),
)
