from django.db import models
from datetime import datetime
from tourer.models import Tourer
from django.urls import reverse
# Create your models here.



class Restaurant(models.Model):
    CITY_CHOICES = (
        ('Đà Nẵng','Đà Nẵng'),
        ('Hà Nội','Hà Nội'),
        ('Hồ Chí Minh','Hồ Chí Minh'),
        ('Đà Lạt','Đà Lạt'),
        ('Nha Trang','Nha Trang'),
        ('Quảng Nam','Quảng Nam'),
        ('Quảng Ngãi','Quảng Ngãi'),
        ('Huế','Huế'),
        ('Gia Lai','Gia Lai'),
        ('Ninh Bình','Ninh Bình'),
        ('Quy Nhơn','Quy Nhơn'),
    )
    TYPE_CHOICES = (
        ('Hải Sản',"Hải Sản"),
        ('Vỉa Hè','Vỉa Hè'),
        ('Nhậu Bình Dân','Nhậu Bình Dân'),
        ('Nhà Hàng','Nhà Hàng'),
        ('Nướng','Nướng')
    )
    name_restaurant = models.CharField(max_length=250)
    # location = models.ForeignKey(City,on_delete=models.CASCADE)
    city = models.CharField(max_length=250,choices=CITY_CHOICES,null=True,blank=True,default='Đà Nẵng')
    address = models.CharField(max_length=250,null=True,blank=True)
    type_restaurant = models.CharField(max_length=250,choices=TYPE_CHOICES,default='Hải Sản')
    image_restaurant = models.FileField(upload_to = 'restaurant/',default='/default/user-avatar-default-165.png')
    review = models.IntegerField(default=0)
    star = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('IndexView_Restaurants')

    def __str__(self):
        return self.name_restaurant + '-' + self.city

class Eating(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name_food = models.CharField(max_length=250)
    info_food = models.CharField(max_length=250)
    price = models.FloatField(default=0,null=True,blank=True)
    img_status = models.FileField(upload_to='restaurant/book/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('IndexView_Eating')

    def __str__(self):
        return self.restaurant.name_restaurant + '-' + self.name_food

class Eating_details(models.Model):
    eating = models.ForeignKey(Eating,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    start_status = models.CharField(max_length=5000)
    end_status = models.CharField(max_length=5000)
    img_status = models.FileField(upload_to='house/book/',default='/default/user-avatar-default-165.png')

    def get_absolute_url(self):
        return reverse('IndexView_Eating_details')

    def __str__(self):
        return self.eating.name_food + '-' + self.title

class Comment_restaurant(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    commnet = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    account = models.ForeignKey(Tourer,on_delete=models.CASCADE)

