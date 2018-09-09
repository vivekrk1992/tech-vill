from maligai import views
from django.conf.urls import url


urlpatterns = [
    url(r'^serve/test/$', views.test),
    url(r'^serve/vehicles/$', views.serve_vehicles),
    url(r'^login/$', views.login),
]
