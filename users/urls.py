from django.urls import path
from .views import register, login, get_all_users

urlpatterns = [
    path('register/', register, name='register'),  # POST
    path('login/', login, name='login'),           # POST
    path('', get_all_users, name='get-all-users'), # GET /api/users/
]
