from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
						url(r'^(?P<board_name>\S+)/$', 'board.views.board_view'),
)
