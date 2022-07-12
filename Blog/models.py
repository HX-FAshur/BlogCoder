from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    pub_date=models.DateField(auto_now_add=True)
    snippet=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self):
        return self.title + '--' + str(self.author)
    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.id)))

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile/")
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    fb_url = models.CharField(max_length=255,null=True,blank=True)
    linkedin_url = models.CharField(max_length=255,null=True,blank=True)
    ig_url = models.CharField(max_length=255,null=True,blank=True)
    pin_url = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home')