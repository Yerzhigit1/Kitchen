from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>', views.index, name='category'),
    path('post/<slug:post_slug>', views.detail_page, name='detail_page'),
]