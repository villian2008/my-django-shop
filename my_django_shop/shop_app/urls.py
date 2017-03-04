""" shop_app URL Configuration """

from django.conf.urls import url
from shop_app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^menu/', views.show_menu, name='menu'),
]
