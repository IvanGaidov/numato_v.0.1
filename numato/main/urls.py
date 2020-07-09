from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [

    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('signup/', views.signup, name='signup'),



]
