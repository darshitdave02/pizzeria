from django.utils import timezone
from django.db import models

# Create a schema such that you’ll design a system for a pizzeria.
# The pizzeria has decided to offer its customers choices for pizza in the following way.
# From an app, a customer can choose
# 1 type of pizza base out of 3 choices (for eg: thin-crust, normal, cheese-burst)
# 1 type of cheese out of 4 choices
# 5 toppings out of 7 choices
# Once the customer has chosen all 7 items (1 base + 1 cheese + 5 toppings), you need to generate an order with these details. Keep in mind that an order can have multiple pizzas. Each pizza will have a fixed price
# The second part of the assignment is tracking the order. For this, you will need to run an asynchronous task which will change the order status based on time in the following way
# Once the order is placed, in the first minute, the status should change from ‘Placed’ to ‘Accepted’
# After 1 minute, the status should change from ‘Accepted’ to ‘Preparing’
# After 3 minutes it should change from ‘Preparing’ to ‘Dispatched’
# After 5 minutes it should read ‘Delivered’

class PizzaBase(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class Cheese(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class Topping(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (
        ('Placed', 'Placed'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    )
    
    pizza_base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE, null=False, blank=False)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, null=False, blank=False)
    toppings = models.ManyToManyField(Topping, null=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Placed')
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Order: {self.id}'
    
class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    status = models.CharField(max_length=10, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Order: {self.order.id} Status: {self.status}'
    
