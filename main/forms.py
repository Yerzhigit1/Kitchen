from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model, password_validation

from main.models import Post
from users.models import CustomUser


class PostCreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [
            'title',
            'photo',
            'category',
            'content',
            'available'
        ]