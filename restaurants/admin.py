from django.contrib import admin
from .models import Restaurant,Eating,Eating_details,Comment_restaurant
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Eating)
admin.site.register(Eating_details)
admin.site.register(Comment_restaurant)
# admin.site.register(Restaurant_tour)