from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),



]