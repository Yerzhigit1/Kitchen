from urllib.parse import urlparse
from django.contrib.messages import success
from django.urls import path, reverse, reverse_lazy
from users import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('main:index')), name="logout"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path("edit/<int:pk>", views.ProfileUpdateView.as_view(), name="edit"),
    
]
