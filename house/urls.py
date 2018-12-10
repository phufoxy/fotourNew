from django.urls import path, re_path,include
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('house/',views.house,name='house'),
    path('error/',views.error_page,name='error_page'),
    path('house/<int:id>/',views.house_details,name='house_details'),
    path('house/search/<str:name>/',views.house_search,name='house_search'),
    path('house/search_house/',views.form_search,name='search_house'),
    path('create_comment_house/<int:id>/',views.create_comment_house,name='create_comment_house'),
    path('create_house_tour/<int:id>/',views.create_house_tour,name='create_house_tour'),
    path('dashboard/home/',views.dashboard_home,name='dashboard_home'),
    path('dashboard/house/',include([
        # houses
        path('',views.ListHouse.as_view(),name='ListHouse'),
        path('create/',views.AddHouse.as_view(),name='AddHouse'),
        path('<int:pk>/delete/',views.DeleteHouse.as_view(),name='house_delete'),
        path('<int:pk>/',views.UpdateHouse.as_view(),name='house_update'),
        path('read/<int:pk>/',views.HouseReadView.as_view(),name='HouseReadView'),
        # House details
        path('details/',views.ListHouseDetails.as_view(),name='ListHouseDetails'),
        path('details/create/',views.AddHouseDetails.as_view(),name='AddHouseDetails'),
        path('details/<int:pk>/delete/',views.DeleteHouseDetails.as_view(),name='HouseDelete_details'),
        path('details/<int:pk>/',views.UpdateHouseDetails.as_view(),name='UpdateHouse_details'),
    ])),
]