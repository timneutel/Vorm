from django.conf.urls import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),
    ('^$', 'website.views.base'),
    ('^admin/', include(admin.site.urls)),
)

import os
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT), 'show_indexes': True}),
    )