from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog_home'),
    path('new/', views.post_new, name='blog_new'),
    path('<int:pk>/', views.post_detail, name='blog_detail'),
    path('<int:pk>/edit/', views.post_edit, name='blog_edit'),
    path('<int:pk>/delete/', views.post_delete, name='blog_delete'),
]
