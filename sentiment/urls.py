from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from sentiment.views import MoodView

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns("",
    url(r'^$', MoodView.as_view(), name="mood"),    
    url(r'^reg/', "sentiment.views.register", name="reg"),
    url(r'^login/', "sentiment.views.login", name="login"),
    url(r'^axis/', "sentiment.views.axis", name="axis"),
)
