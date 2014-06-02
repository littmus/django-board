from django.conf.urls import patterns, include, url
from .views import BoardView

urlpatterns = patterns('',
                        url(r'^(?P<board_pk>\d+)/$', BoardView.as_view()),
)
