"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Epolice_django.views import *

app_name = 'citizen'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('complain/',complaint,name='complaint'),
    path('login/',citizen_login,name='login'),
    path('about/',about,name='about'),
    path('services/',services,name='services'),
    path('contact/',contact,name='contact'),
    path('logout/',citizen_logout,name='logout'),
    path('status/',status,name='status'),
    path('register/',citizen_register,name='register'),
    path('submit_complaint/',submit_complaint,name='submit_complaint'),
    path('citizen_otp/',citizen_otp, name='otp'),
    path('view_form/<int:cid>',view_form, name='view_form'),
]