from django.core import *
from django.http import HttpResponse
from django.db import models
from .models import Category
from django.shortcuts import render


# Create your views here.

def home(request):

    glav_categories = Category.objects.filter(parent=None)
    all_childrens = Category.objects.exclude(parent=None).order_by('parent')

    menu = '<ul>'
    categories = glav_categories

    def find_child(parent):
        nonlocal menu
        menu = menu +'<ul>'
        for podcat in all_childrens:
            if podcat.parent == parent:
                menu = menu +'<li>'+podcat.title+'</li>'
                find_child(podcat)
        menu = menu +'</ul>'
        menu = menu.replace('<ul></ul>', '')

    for glav_cat in glav_categories:
        menu = menu +'<li>'+glav_cat.title+'</li>'
        find_child(glav_cat)
    menu = menu +'</ul>'

    context = {'categories': categories, 'menu': menu}
    return render(request, 'shop_app/index.html', context)
