from django.db import models
from datetime import datetime    
from django.urls import reverse
# from django.forms import CharField, Form, PasswordInput
# Create your models here.
class Tourer(models.Model):
    ACCOUNT_CHOICES = (
        ('admin','admin'),
        ('account','account'),
    )
    email = models.CharField(max_length=250,blank=True,primary_key=True)
    name = models.CharField(max_length = 250)
    avatar = models.FileField(upload_to = 'tourer/',default='/default/avatar.jpg')
    password = models.CharField(max_length=250)
    question = models.CharField(max_length=250,default='question')
    author = models.CharField(max_length=250,choices=ACCOUNT_CHOICES,null=True,blank=True,default='account')


    def __str__(self):
        return self.name
    
class Account(models.Model):
    ACCOUNT_CHOICES = (
        ('admin','admin'),
        ('account','account'),
    )
    email = models.CharField(max_length=250)
    name = models.CharField(max_length = 250)
    avatar = models.FileField(upload_to = 'tourer/',default='/default/avatar.jpg')
    password = models.CharField(max_length=250)
    question = models.CharField(max_length=250,default='question')
    description = models.CharField(max_length=250,default='Funny')
    author = models.CharField(max_length=250,choices=ACCOUNT_CHOICES,null=True,blank=True,default='account')
    


    def __str__(self):
        return self.name