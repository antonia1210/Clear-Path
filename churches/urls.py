from django.urls import path
from . import views

app_name = 'churches'
urlpatterns = [
    path('', views.ChurchesListView.as_view(), name='list'),
    path('<int:church_id>/', views.ChurchesItemListView.as_view(), name='items'),
]