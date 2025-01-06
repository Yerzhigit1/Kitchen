from urllib import request
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from main.models import Post
from users.forms import RegisterForm, UserUpdateForm

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = "Вы успешно зарегистрировались! Теперь войдите в свой аккаунт."

    
class ProfileView(LoginRequiredMixin, DetailView):
    template_name= 'users/profile.html'
    model = get_user_model()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts_by_author"] = Post.objects.filter(author=self.request.user)
        return context
    
    
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = get_user_model()
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('main:index')
    

    