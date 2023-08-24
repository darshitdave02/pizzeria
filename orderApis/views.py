from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect
from django.urls import reverse
from orderApis.tasks import update_order_status
from .serializers import OrderSerializer, PizzaBaseSerializer, CheeseSerializer, ToppingSerializer, PizzaSerializer
from .models import Order, PizzaBase, Cheese, Topping, Pizza
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import schema


def index(request):
    cheeses = Cheese.objects.all()
    pizza_bases = PizzaBase.objects.all()
    toppings = Topping.objects.all()
    
    context = {

        'cheeses': cheeses,
        'pizza_bases': pizza_bases,
        'toppings': toppings,
    }
    return render(request, 'index.html', context)


@api_view(['GET'])
def orderList(request):
    try:
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def cheeseList(request):
    try:
        cheeses = Cheese.objects.all()
        serializer = CheeseSerializer(cheeses, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def orderList(request):
    try:
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def pizzaList(request):
    pizzas = Pizza.objects.all()
    serializer = PizzaSerializer(pizzas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pizzaBaseList(request):
    try:
        pizzaBases = PizzaBase.objects.all()
        serializer = PizzaBaseSerializer(pizzaBases, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def toppingList(request):
    try:
        toppings = Topping.objects.all()
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method='POST',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['pizza_base', 'cheese', 'toppings'],
        properties={
            'pizza_base': openapi.Schema(type=openapi.TYPE_INTEGER),
            'cheese': openapi.Schema(type=openapi.TYPE_INTEGER),
            'toppings': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER)),
        },
    ),
    responses={200: 'Success', 400: 'Bad Request'}
)
@api_view(['POST'])
def orderCreate(request):
    try:

        pizza_base_id = request.data.get('pizza_base')
        cheese_id = request.data.get('cheese')
        topping_ids = request.data.getlist('toppings')
        
        # Check if required data is provided
        if pizza_base_id is None or cheese_id is None or not topping_ids:
            return Response({'error': 'Required data missing in request body'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            pizza_base = PizzaBase.objects.get(id=pizza_base_id)
            cheese = Cheese.objects.get(id=cheese_id)
            toppings = Topping.objects.filter(id__in=topping_ids)
        except (PizzaBase.DoesNotExist, Cheese.DoesNotExist):
            return Response({'error': 'Invalid pizza base or cheese ID'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Ensure at least 5 toppings are provided
        if toppings.count() < 5:
            return Response({'error': 'At least 5 toppings are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Calculate pizza price
        pizza_price = pizza_base.price + cheese.price + sum(topping.price for topping in toppings)
        
        # Create pizza
        pizza = Pizza.objects.create(
            pizza_base=pizza_base,
            cheese=cheese,
            price=pizza_price
        )
        
        # Calculate total price
        total_price = pizza_price
        
        # Create order and add pizza
        order = Order.objects.create(total_price=total_price)
        order.pizzas.add(pizza)
        order.save()
        
        serializer = OrderSerializer(order)  # Serialize the created order
        update_order_status.delay(order.id, order.created_at)  # Start the task
        return render(request, 'order_create.html', {'order': order})
        return Response({'message': 'Order created successfully', 'order': serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def orderStatus(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


