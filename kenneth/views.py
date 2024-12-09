from django.shortcuts import render
from .models import Category, Skills

# Create your views here.

def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'index.html')