from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="landing"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^pokes$', views.success, name="dashboard"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^pokes/(?P<id>\d+)$', views.pokes, name="pokes"),
]
