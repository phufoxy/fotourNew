from django.urls import path, re_path,include
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('book/',views.book,name='book'),
    path('book_details/',views.book_details,name='book_details'),
    path('dashboard/book/',include([
        path('',views.ListBookTour.as_view(),name='ListBookTour'),
        path('create/',views.AddBookTour.as_view(),name='AddBookTour'),
        path('<int:pk>/',views.UpdateBookTour.as_view(),name='UpdateBookTour'),
        path('<int:pk>/delete/',views.DeleteBookTour.as_view(),name='DeleteBookTour'),
        path('read/<int:pk>/',views.BookTourReadView.as_view(),name='BookTourReadView'),
    ]))
]