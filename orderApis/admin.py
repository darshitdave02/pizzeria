from django.contrib import admin
from .models import Order, PizzaBase, Cheese, Topping, OrderStatus
# Register your models here.

admin.site.register(Order)
admin.site.register(PizzaBase)
admin.site.register(Cheese)
admin.site.register(Topping)
admin.site.register(OrderStatus)

