from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('',views.IndexTemplate.as_view(), name='index'),
    path('myblog/',views.BlogTemplate.as_view(), name= 'myblog'),
    path('single/',views.SIngleTemplate.as_view(), name= 'single'),
    path('login/',views.LoginTemplate.as_view(), name= 'login'),

]