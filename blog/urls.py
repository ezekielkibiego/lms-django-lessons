from django.urls import path
from .views import *

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('add-blog', add_blog, name='add-blog'),
    path('blogs/', blog, name='blog'),
]