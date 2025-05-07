from django.urls import path
from .views import index, students_list

urlpatterns = [
    path('', index, name='index'),
    path('students/', students_list, name='students'),
    
]