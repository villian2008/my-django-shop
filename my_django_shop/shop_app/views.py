from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.

def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'shop_app/index.html', context)
