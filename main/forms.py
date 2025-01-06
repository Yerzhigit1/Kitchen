from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.forms import fields

from main.models import Post
from users.models import CustomUser

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'category']
        
        
class SearchForm(forms.Form):
    q = forms.CharField(max_length=100)
    
    # def search(self):
    #     search = self.cleaned_data.get('search')
    #     return Post.objects.filter(
    #         Q(title__icontains=search) | Q(content__icontains=search)
    #     )
    
    
class PostUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'category']