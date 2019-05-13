
from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('home/', views.home),
    re_path(r'^$', views.article_list),
]
