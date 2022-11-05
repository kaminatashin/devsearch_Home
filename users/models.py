from argparse import _MutuallyExclusiveGroup
from email.policy import default
from operator import truediv
from pickle import TRUE
import profile
from pyexpat import model
from tkinter.tix import Tree
from unicodedata import name
from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Profiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=500,blank=True,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    short_intro=models.CharField(max_length=200,blank=True,null=True)
    username=models.CharField(max_length=40)
    location=models.TextField(null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    profile_image=models.ImageField(blank=True,null=True,upload_to='profiles/', default='profiles/user-default.png')
    social_github=models.CharField(max_length=2000,null=True,blank=True)
    social_twitter=models.CharField(max_length=2000,null=True,blank=True)
    socail_linkedin=models.CharField(max_length=2000,null=True,blank=True)
    social_youtube=models.CharField(max_length=2000,null=True,blank=True)
    social_website=models.CharField(max_length=2000,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,editable=False)
    id=models.UUIDField(default= uuid.uuid4,unique=True,primary_key=True,editable=False)  
    def __str__(self):
        return str(self.user.username)
    class Meta:
       ordering=['created']  

    @property
    def imageURL(self):
        try:
            url=self.profile_image.url
        except:
            url=''  
        return url    
        

class Skill(models.Model) :
    owner=models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,editable=False)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    def __str__(self):
        return str(self.name)

class Message(models.Model):
    sender=models.ForeignKey(Profiles,on_delete=models.SET_NULL,blank=True,null=True)
    recipient=models.ForeignKey(Profiles,on_delete=models.SET_NULL,blank=True,null=True,
                                 related_name='messages')
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    subject=models.CharField(max_length=200,null=True,blank=True)
    body=models.TextField()
    is_read=models.BooleanField(default=False,null=True)
    created=models.DateTimeField(auto_now_add=True,editable=False)
    id=models.UUIDField(default= uuid.uuid4,unique=True,
                            primary_key=True,editable=False)  
    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering=['is_read', '-created']    
    
# class Users(models.Model):
#     id=models.UUIDField(uuid.uuid4,primary_key=True,unique=True,editable=False)
#     user_name=models.CharField(max_length=80)
#     email=models.EmailField(max_length=80)
#     first_name=models.CharField(max_length=80)
#     last_name=models.CharField(max_length=80)
#     is_staff=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)
