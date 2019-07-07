# Blog URLS file

from django.urls import path
from . import views   # Import view from BLOG (. means current directory)

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
