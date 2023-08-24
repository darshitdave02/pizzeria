from django.http import HttpResponseNotFound
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cheese', views.cheeseList, name='cheese-list'),
    path('order', views.orderList, name='order-list'),
    path('pizza', views.pizzaList, name='pizza-list'),
    path('pizzaBase', views.pizzaBaseList, name='pizzaBase-list'),
    path('topping', views.toppingList, name='topping-list'),
    path('createOrder', views.orderCreate, name='order-create'),
    path('status/<int:order_id>', views.orderStatus, name='order-status'),

]