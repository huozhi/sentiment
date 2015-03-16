from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from sentiment.views import MoodView

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns("",
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^reg/', "sentiment.views.register", name="reg"),
    url(r'^login/', "sentiment.views.login", name="login"),
    url(r'^mood/$', MoodView.as_view(), name="mood"),
    url(r'^axis/', "sentiment.views.axis", name="axis"),
    # url(r'^post/', "sentiment.views.post_mood", name="post_mood"),

    # test
    url(r'test/', "sentiment.views.test", name="test"),
)
