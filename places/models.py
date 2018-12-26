from django.db import models
from datetime import datetime
from tourer.models import Tourer, Account
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextFormField

# Create your models here.
class TypePlace(models.Model):
    TYPE_PLACE = (
        ('Cầu','Cầu'),
        ('Sông','Sông'),
        ('Hồ','Hồ'),
        ('Núi','Núi'),
        ('Biển','Biển')
    )
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
    city = models.CharField(max_length=250,null=True,blank=True,choices=CITY_CHOICES,default='Đà Nẵng')
    address = models.CharField(max_length=250,null=True,blank=True)
    type_place = models.CharField(max_length=250,choices=TYPE_PLACE,default='Núi')

    class Meta:
        abstract = True


#  implement a prototype pattern
# factory
class Place(TypePlace):
    name_place = models.CharField(max_length=250)
    image_place = models.FileField(upload_to = 'place/',default='/default/user-avatar-default-165.png')
    review = models.IntegerField(default=0)
    star = models.FloatField(default=0)
    price = models.FloatField(default=0,null=True,blank=True)
    content = models.CharField(max_length=1250)


    def get_absolute_url(self):
        return reverse('ListPlace')

    def __str__(self):
        return self.name_place + '-' + self.city

class TypeDetails(models.Model):
    body = RichTextUploadingField()

    class Meta:
        abstract = True

class PlaceDetails(TypeDetails):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)


    def __str__(self):
        return self.place.name_place 

class ItemComment(models.Model):
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        abstract = True

    def __str__(self):
        return self.comment 

class CommentPlace(ItemComment):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    


class Email(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

class Products(models.Model):
    content = RichTextFormField()