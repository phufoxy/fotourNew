from django.urls import path,include
from . import views
urlpatterns = [
    path('',include([
        path('',views.home,name='home'),
        path('search/',views.search_multi,name='tour_mutil')
    ]))
    
]