from django.urls import path
from django.conf.urls import include, url, re_path, include

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.BlogView.as_view(), name='blog')
]