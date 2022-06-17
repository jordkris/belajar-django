from django.urls import path
from finalboss import views

urlpatterns = [
    path('', views.users, name='users'),
    path('<str:username>', views.userDetail, name='userDetail'),
    path('<str:username>/edit', views.editProfile, name='editProfile'),
    path('<str:username>/buy', views.buyReksaDana, name='buyReksaDana'),
    path('<str:username>/details', views.detailReksaDana, name='detailReksaDana'),
    path('<str:username>/sell/<str:id>', views.sellReksaDana, name='sellReksaDana'),
]