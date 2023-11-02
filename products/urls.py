from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('cart_page/', views.cart_page, name='cart_page')
]
