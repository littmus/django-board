from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
						url(r'^join/$', 'account.views.join_view'),
						url(r'^join_ok/$', 'account.views.join_ok'),
)
