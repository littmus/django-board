from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
			url(r'^$', 'kuics.views.index'),
			url(r'^admin/', include(admin.site.urls)),
			url(r'^account/', include('account.urls')),
            url(r'^board/', include('board.urls')),
            url(r'^article/', include('article.urls')),
    # Examples:
    # url(r'^$', 'kuics.views.home', name='home'),
    # url(r'^kuics/', include('kuics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:\
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
