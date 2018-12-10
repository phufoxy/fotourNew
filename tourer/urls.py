from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.login,name='login'),
    path('login/login_form/',views.login_form,name='login_form'),
    path('login/register/',views.register_main,name='Register'),
    path('login/logout/',views.logout,name='logout'),
    path('login/signup/',views.form_signup,name='signup'),
    path('login/forget/',views.forget,name='forget'),
    path('login/form_forget/',views.form_forget,name='form_forget'),
    # dashboard
    path('dashboard/account/',include([
        # tour
        path('',views.ListAccount.as_view(),name='ListAccount'),
        path('create/',views.AddAccount.as_view(),name='AddAccount'),
        path('<int:pk>',views.UpdateAccount.as_view(),name='UpdateAccount'),
        path('<int:pk>/delete/',views.DeleteAccount.as_view(),name='DeleteAccount'),
        path('read/<int:pk>/',views.AccountReadView.as_view(),name='AccountReadView'),
    ])),
]