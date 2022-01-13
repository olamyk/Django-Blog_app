from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create',views.CreateUser.as_view(),name= 'register'),
    path('user/detail/view/<int:pk>',views.UserDetailView.as_view(),name= 'profile'),
    path('add/profile',views.UserAddProfile.as_view(),name= 'add_profile'),
    path('user/update/<int:pk>',views.profile,name= 'user_update'),

    path('change_password',auth_views.PasswordResetView.as_view(template_name ='registration/password_change.html'),name= 'change_password'),
]