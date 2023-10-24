from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_invoice, name='add'),
    path('list/', list_invoice, name='list'),
    path('update/<str:pk>/', update_invoice, name="update"),
    path('delete/<str:pk>/', delete_invoice, name="delete"),
]

   