
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("You are logged in!")

def accountant_view(request):
    return HttpResponse("This is the page for the accountant. You are logged in")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path("home/", home, name="home"),
    path("items/", include('items.urls')),
    path("churches/", include('churches.urls')),

]
