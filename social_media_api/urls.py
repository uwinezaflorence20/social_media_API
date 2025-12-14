from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home),  # 👈 HOME PAGE
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
]
