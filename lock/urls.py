from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('',views.lockhome,name='lockhome'),
        path('login/',views.login,name='login'),
        path('sign/',views.sign,name='sign'),
        path('logout/',views.logout,name='logout'),
        path('joboffers/',views.post_a_job,name='post_a_job'),
        path('profile/',views.profile,name='profile'),
]