from django.urls import path, re_path
from . import views
import django.views.defaults

urlpatterns = [
    path('learn/',views.index,name='learn'),
]