# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:id>/edit/', views.post_edit, name='post-edit'),
    path('post/<int:id>/delete/', views.post_delete, name='post-delete'),
]


