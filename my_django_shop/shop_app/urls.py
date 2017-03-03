""" shop_app URL Configuration """

from django.conf.urls import url, include
from django.contrib import admin
from shop_app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
