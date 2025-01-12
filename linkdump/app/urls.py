from django.urls import path
from . import views

urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('link/new/', views.link_create, name='link_create'),
    path('link/<int:pk>/edit/', views.link_update, name='link_update'),
    path('link/<int:pk>/delete/', views.link_delete, name='link_delete'),
]