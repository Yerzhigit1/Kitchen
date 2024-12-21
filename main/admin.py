from django.contrib import admin
from main.models import Category, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'category', 'content', 'photo', 'available']
    list_display = ['title', 'content', 'category', 'created_at', 'available']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}