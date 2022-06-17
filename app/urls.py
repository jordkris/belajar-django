from django.urls import path
from app import views

urlpatterns = [
    path('all/', views.customer, name='customer'),
]