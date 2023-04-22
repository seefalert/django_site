"""url patterns"""
# pylint: disable=import-error

from django.urls import path

from mysite.blog import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
