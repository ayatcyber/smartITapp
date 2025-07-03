# students/urls.py

from django.urls import path
from .views import create_student

urlpatterns = [
    path('register/', create_student, name='create_student'),
]
