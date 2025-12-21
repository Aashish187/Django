"""
URL configuration for studybud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse


 #fucntion based url routing can be messy to create large number of fucntions in this fil
# def home(response):
#     return HttpResponse("Home")

# def another(response):
#     return HttpResponse("This is another page")
# we will seperately do all this from the apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('base.urls'))
    # path("",home),
    # path("page/",another)
]
