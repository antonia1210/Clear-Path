from django.urls import path
from . import views
from .views import export_to_csv, accountant_export_to_csv

app_name = 'items'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='list'),
    path('create/', views.ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
    path('export', export_to_csv, name='export'),
    path('acc_export/<int:church_id>', accountant_export_to_csv, name='acc_export'),
]