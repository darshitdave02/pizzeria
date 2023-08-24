from rest_framework import serializers
from .models import Order, PizzaBase, Cheese, Topping, Pizza

class PizzaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaBase
        fields = '__all__'

class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = '__all__'

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'