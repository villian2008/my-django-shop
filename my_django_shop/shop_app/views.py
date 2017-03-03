from django.shortcuts import render
from django.core import *
from django.http import HttpResponse
from .models import Category
from django.db import models

# Create your views here.

def home(request):
    glav_categories = Category.objects.filter(parent=None)

    categories = Category.objects.filter(parent=None)
    context = {'categories': categories}
    return render(request, 'shop_app/index.html', context)
