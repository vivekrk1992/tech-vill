from django.conf.urls import url
from uram import views
from main.views import login


urlpatterns = [

    # mobile login
    url(r'^login/$', login),
]
