from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_images/%Y/%m/%d', blank=True, null=True)
    phonenumber = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.id})
    
