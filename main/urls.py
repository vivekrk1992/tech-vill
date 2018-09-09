from main.views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', login),
    url(r'^test/$', test),
]
