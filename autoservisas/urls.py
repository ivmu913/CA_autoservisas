from django.urls import path
from . import views

urlpatterns = [
    # indexas where all card are displayed
    path('', views.index, name='index'),
    # page to display all services
    path('cars/', views.cars, name='cars'),
    # detail display if car
    path('<int:car_id>/car_id', views.specific_car, name='specific_car'),
    # ALL SERVICES
    path('services/', views.services, name='services'),
    # ALL ORDERS
    path('orders/', views.orders, name='orders'),
    # specific order
    path('<int:order_id>/order_id', views.specific_order, name='specific_order'),
]