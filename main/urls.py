from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>', views.index, name='category'),
]