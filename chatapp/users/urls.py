from django.urls import path
from .views import CustomUser

app_name = 'users'
urlpatterns = [
    path('register/', CustomUser.as_view(), name='register'),
]