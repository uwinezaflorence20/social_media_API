from django.urls import path
from .views import register, login,get_all_users

urlpatterns = [
    path('register/', register),
    path('login/', login),
   path('users/',get_all_users),
]
