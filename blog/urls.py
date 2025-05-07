from django.urls import path
from .views import *

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('add-blog', add_blog, name='add-blog'),
    path('blogs/', blog, name='blog'),
    path('blogs/<int:pk>/edit/', update_blog, name='update_blog'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),
]