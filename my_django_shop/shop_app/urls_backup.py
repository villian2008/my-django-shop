"""Резервная копия корневой конфигурации URL проекта my_django_shop.

Исходный файл: my_django_shop/my_django_shop/urls.py
Скопировано для демонстрации записи в другой каталог репозитория.
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop_app/', include('shop_app.urls')),
]
