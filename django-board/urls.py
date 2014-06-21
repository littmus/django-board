from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/', include('article.urls')),
    url(r'^board/', include('board.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
)
