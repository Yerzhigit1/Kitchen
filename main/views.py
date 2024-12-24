from turtle import pos
from unicodedata import category
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import ListView
from .models import Post, Category

# class IndexView(ListView):
#     template_name = 'main/index.html'
#     model = ...
#     context_object_name = ...
    
    
def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    data = {
        'title': 'Home',
        'posts': posts,
        'categories': categories,
        'category': category
    }
    return render(request, 'main/index.html', data)


def detail_page(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    data = {
        'post': post
    }
    return render(request, 'main/detail_page.html', data)

# def category_view(request, category_slug):
#     posts_by_cat = Post.objects.filter(category__slug=category_slug)
#     category = Category.objects.filter(slug=category_slug)
#     data = {
#         'category': category,
#         'posts_by_cat': posts_by_cat,
#     }
#     return render(request, 'main/index.html', data)