from django.contrib import admin
from .models import Tour, BookTour, PlaceTour, HouseTour
# Register your models here.
admin.site.register(Tour)
admin.site.register(BookTour)
admin.site.register(PlaceTour)
admin.site.register(HouseTour)