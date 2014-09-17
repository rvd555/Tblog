from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # url(r'^$', 'tblog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^blog/', include('apps.blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )


urlpatterns += patterns(
    '',
    url(r'^400/$', 'django.views.defaults.bad_request'),
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),
)


# added by Tulpar,20140514
from django.conf import settings

urlpatterns += patterns('',
                        url(r"^media/(?P<path>.*)$",
                            "django.views.static.serve",
                            {"document_root": settings.MEDIA_ROOT}
                            ),
                        )

urlpatterns += patterns('',
                        url(r"^static/(?P<path>.*)$",
                            "django.views.static.serve",
                            {"document_root": settings.STATIC_ROOT}
                            ),
                        )
