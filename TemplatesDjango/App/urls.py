from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contacts/', contacts),
]
