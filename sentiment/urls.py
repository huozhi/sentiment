from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sentiment.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/$', 'sentiment.views.register', name='reg'),
    url(r'^login/$', 'sentiment.views.login', name='login'),
    url(r'^user/$', 'sentiment.views.usermood', name='user_mood'),
    url(r'^axis/', 'sentiment.views.axis', name='axis'),
)
