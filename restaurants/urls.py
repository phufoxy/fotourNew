from django.urls import path, re_path,include
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    # home
    path('restaurant/',include([
        path('',views.index,name='restaurant'),
        path('<int:id>/',views.eating,name='eating'),
        path('search/<str:name>/',views.index_city,name='search_restaurant'),
        path('search_form/',views.search_form,name='search_form'),
        path('create_comment_eating/<int:id>/',views.create_comment_eating,name='create_comment_eating'),
        path('<int:id>/eating/<int:id_restaurant>/',views.eating_details,name='eating_details'),
        path('create_restaurant_tour/<int:id>/',views.create_restaurant_tour,name='create_restaurant_tour'),
    ])),
    # dashboard
    path('dashboard/restaurants/',include([
        # restaurants
        path('',views.ListRestaurants.as_view(),name='IndexView_Restaurants'),
        path('create/',views.AddRestaurants.as_view(),name='CreateRestaurant'),
        path('<int:pk>/',views.UpdateRestaurant.as_view(),name='UpdateRestaurant'),
        path('<int:pk>/delete/',views.DeleteRestaurant.as_view(),name='RestaurantDelete'),
        # eating
        path('eating/',include([
            path('',views.ListEating.as_view(),name='IndexView_Eating'),
            path('create/',views.AddEating.as_view(),name='CreateEating'),
            path('<int:pk>/',views.UpdateEating.as_view(),name='UpdateEating'),
            path('<int:pk>/delete/',views.DeleteEating.as_view(),name='EatingDelete'),
            # details
            path('details/',include([
                # eating_details
                path('',views.ListEatingDetails.as_view(),name='IndexView_Eating_details'),
                path('create/',views.AddEatingDetails.as_view(),name='CreateEating_details'),
                path('<int:pk>/',views.UpdateEatingDetail.as_view(),name='UpdateEating_details'),
                path('<int:pk>/delete/',views.DeleteEatingDetails.as_view(),name='Eating_detailsDelete'),
            ])),
        ])),
    ])),
]