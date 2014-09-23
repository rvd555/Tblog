from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import home, detail, category_articles, tag_articles

urlpatterns = patterns('',
                       # Examples:
                       url(r'^index$', home, name='home'),
                       url(r'^category/(?P<category_name>\w+)/$',
                           category_articles,
                           name='category_articles'
                           ),
                       url(r'^tag/(?P<tag_name>\w+)/$',
                           tag_articles,
                           name='tag_articles'
                           ),
                       url(r'^detail/(?P<id>\d)/$', detail, name='detail'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       )
