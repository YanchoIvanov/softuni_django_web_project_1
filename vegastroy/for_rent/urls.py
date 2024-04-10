from django.urls import path
from . import views


urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_details, name='item_details'),
    path('item/<int:pk>/success/', views.success_for_rent, name='success_for_rent'),

]
