from django.utils import timezone
from django.db import models

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

class Pizza(models.Model):
    pizza_base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE, null=False, blank=False)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, null=False, blank=False)
    toppings = models.ManyToManyField(Topping, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'Pizza: {self.id}'
 
class Order(models.Model):
    STATUS_CHOICES = (
        ('Placed', 'Placed'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    )
    
    pizzas = models.ManyToManyField(Pizza)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Placed')
    total_price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Order: {self.id}'
 