from django.contrib import admin
from .models import House,House_details,Comment_house
# Register your models here.
admin.site.register(House)
admin.site.register(House_details)
# admin.site.register(Room)
admin.site.register(Comment_house)
# admin.site.register(House_tour)