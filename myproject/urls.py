"""
URL configuration for myproject project.

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
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("You are logged in!")

def user_view(request):
    return HttpResponse("This is the page for users. You are logged in")

def accountant_view(request):
    return HttpResponse("This is the page for the accountant. You are logged in")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path("home/", home, name="home"),
    path("user/", user_view, name="user"),
    path("account/", accountant_view, name="accountant"),
]
