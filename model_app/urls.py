from django.urls import path

from . import views

urlpatterns = [
    path('index', views.calculate, name='calculate'),
]