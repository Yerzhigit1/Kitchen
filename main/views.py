from turtle import pos
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category

class IndexView(ListView):
    template_name = 'main/index.html'
    model = ...
    context_object_name = ...
    
    
# def index(request):
#     posts = Post.objects.filter(available=True)
#     categories = Category.objects.all()
#     data = {
#         'title': 'Home',
#         'posts': posts,
#         'categories': categories
#     }
#     return render(request, 'main/index.html', data)


def category_view(request, category_slug):
    posts_by_cat = Post.objects.filter(category__slug=category_slug)
    category = Category.objects.filter(slug=category_slug)
    data = {
        'category': category,
        'posts_by_cat': posts_by_cat,
    }
    return render(request, 'main/index.html', data)