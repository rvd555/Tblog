from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import home, detail

urlpatterns = patterns('',
                       # Examples:
                       url(r'^index$', home, name='home'),
                       # url(r'^category/(?P<category_name>)$', category, name='category'),
                       url(r'^detail/(?P<id>\d)/$', detail, name='detail'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       )
