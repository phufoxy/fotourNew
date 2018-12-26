from django.contrib import admin
from .models import Place,PlaceDetails,CommentPlace,Email, Products
# Register your models here.
admin.site.register(Place)
admin.site.register(PlaceDetails)
admin.site.register(CommentPlace)
admin.site.register(Email)
admin.site.register(Products)