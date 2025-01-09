from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from users.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='photo/%y/%m/%d', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_posts')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("main:detail_page", kwargs={"post_slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
        
        
class Category(models.Model):
    name= models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:category', kwargs={"category_slug": self.slug})
    
    
# class CustomUser(AbstractUser):
#     birth_date = models.DateField(blank=True, null=True)
#     phonenumber = models.CharField(max_length=15, blank=True) 
#     avatar = models.ImageField(upload_to='avatars/', blank=True)

#     def __str__(self):
#         return self.username

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_for_posts')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments_by_author')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post.title[:20]}"