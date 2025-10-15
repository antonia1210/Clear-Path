from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='list'),
    path('create/', views.ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
]