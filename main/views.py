from pdb import post_mortem
from turtle import pos
from unicodedata import category
from urllib import request
from urllib.parse import urlencode
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


from main.forms import PostComments, PostCreateForm, SearchForm, PostUpdateForm
from .models import Post, Category, Comment

# class IndexView(ListView):
#     template_name = 'main/index.html'
#     model = ...
#     context_object_name = ...
    
    
# def index(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     posts = Post.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         posts = posts.filter(category=category)
#     data = {
#         'title': 'Home',
#         'posts': posts,
#         'categories': categories,
#         'category': category
#     }
#     return render(request, 'main/index.html', data)


class MainView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Home'}
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.filter(available=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
            self.extra_context['category'] = category
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
        })
        context.update(self.extra_context)
        return context
    


# def detail_page(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#     data = {
#         'post': post
#     }
#     return render(request, 'main/detail_page.html', data)

class DetailPage(DetailView):
    template_name = 'main/detail_page.html'
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пост'
        current_post = get_object_or_404(Post, slug=self.kwargs.get('post_slug'))
        if self.request.user.is_authenticated:
            current_author_comments = list(self.request.user.comments_by_author.filter(post=current_post).order_by('-created_at'))
            other_comments = list(current_post.comments_for_posts.exclude(author=self.request.user).order_by('-created_at'))
            context['all_comments'] = current_author_comments + other_comments
        else:
            context['all_comments'] = current_post.comments_for_posts.order_by('-created_at')
        context['form'] = PostComments()
        return context
    
    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            messages.info(request, 'Для того чтобы оставить комментарий, войдите в свой аккаунт')
            current_url = request.build_absolute_uri()
            login_url = f"{reverse('users:login')}?{urlencode({'next': current_url})}"
            return redirect(login_url)
        
        current_post = get_object_or_404(Post, slug=self.kwargs.get('post_slug'))
        form = PostComments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = current_post
            comment.author = request.user
            comment.save()
            return redirect('main:detail_page', post_slug=current_post.slug)
        context = self.get_context_data()
        context['form'] = form  # Возвращаем форму с ошибками
        return self.render_to_response(context)
    
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostUpdateForm
    template_name  = 'main/update_post.html'
    context_object_name = 'post'
    model = Post
    slug_url_kwarg = 'post_slug'
    
    def get_success_url(self):
        return reverse_lazy('main:detail_page', kwargs={'post_slug': self.object.slug})
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('main:index')
    template_name = 'main/delete_post.html'
    context_object_name = 'post'
    

class PostAddView(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('main:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить пост'
        context['categories'] = Category.objects.all()
        return context


class SearchView(ListView):
    template_name = 'main/index.html'
    form_class = SearchForm
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    
    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data.get('q')
            return Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return Post.objects.none()
