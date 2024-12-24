from urllib.parse import urlparse
from django.urls import path
from users import views
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login')
]
