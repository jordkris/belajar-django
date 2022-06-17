from django.urls import path
from app import views

urlpatterns = [
    path('', views.customer, name='customer'),
    path('add/', views.addCustomerForm, name='addCustomer'),
    path('detail/<str:key>', views.detailCustomer, name='detailCustomer'),
    path('delete/<str:key>', views.deleteCustomer, name='deleteCustomer'),
]