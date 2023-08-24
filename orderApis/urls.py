from django.urls import path

from . import views

urlpatterns = [
    
    path('cheese', views.cheeseList, name='cheese-list'),
    path('order', views.orderList, name='order-list'),
    path('pizza', views.pizzaList, name='pizza-list'),
    path('pizzaBase', views.pizzaBaseList, name='pizzaBase-list'),
    path('topping', views.toppingList, name='topping-list'),
    path('createOrder', views.orderCreate, name='order-creat'),
    path('status/<int:order_id>', views.orderStatus, name='order-status'),


]