from django.db import models as jimmy
from django.contrib.auth.models import User
from PIL import Image
from blogApp.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user    = models.OneToOneField(User,null= True, on_delete=models.CASCADE)
    pic     = models.ImageField(upload_to='featured_images',blank=True)
    bio     = models.TextField()
    address = models.TextField(max_length= 200)


class TextThings(jimmy.Model):
    user = jimmy.CharField(max_length = 100) # which means i can use something like this

