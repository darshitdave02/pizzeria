from django.http import HttpResponseNotFound
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cheese', views.cheeseList, name='cheese-list'),
    path('orders', views.orderList, name='order-list'),
    path('pizzas', views.pizzaList, name='pizza-list'),
    path('pizzaBase', views.pizzaBaseList, name='pizzaBase-list'),
    path('toppings', views.toppingList, name='topping-list'),
    path('createOrder', views.orderCreate, name='order-create'),
    path('status/<int:order_id>', views.orderStatus, name='order-status'),

]