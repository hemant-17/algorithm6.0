from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name='index'),
    path('', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('sign/',views.sign,name='sign'),
    path('logout/',views.logout,name='logout'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    path('ui/',views.ui,name='ui'),
    path("display/<int:id>", views.display, name="display"),
    path('profile/<str:user>/',views.Profile, name="profile"),
    path('courses/',views.courses,name='courses'),
    path('courses/nptel/',views.course1,name='course1'),
    path('Jobs/',views.jobs,name='jobs'),
    path('quiz/',views.quiz,name='quiz'),
    path('apply/<str:email1>/<str:jobtitle1>/<str:username2>/',views.apply,name="apply"),

    path('jobview/<str:Comp>/<str:jobtitle>/<str:username1>',views.jobview,name="jobview"),
]