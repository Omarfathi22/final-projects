from django.urls import path
from . import views


urlpatterns = [ 

    path('', views.store, name='store'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customer', views.customer_list, name='customer_list'),
    path('index/', views.front, name='front'),
    path('category/', views.category_view, name='category_view'),
    path('order/', views.order_view, name='order_view'),
]
