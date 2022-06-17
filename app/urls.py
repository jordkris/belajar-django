from django.urls import path
from app import views

urlpatterns = [
    path('', views.customer, name='customer'),
    path('new/', views.newCustomerForm, name='newCustomer'),
]