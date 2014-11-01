from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sentiment.views.index', name='index'),
    url(r'^reg/', 'sentiment.views.register', name='reg'),
    url(r'^login/', 'sentiment.views.login', name='login'),
    url(r'^mood/$', 'sentiment.views.user_mood', name='user_mood'),
    url(r'^axis/', 'sentiment.views.axis', name='axis'),
    url(r'^post/', 'sentiment.views.post_mood', name='post_mood'),

    # test
    url(r'test/', 'sentiment.views.test', name='test'),
)
