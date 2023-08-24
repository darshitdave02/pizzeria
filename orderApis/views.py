from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OrderSerializer, PizzaBaseSerializer, CheeseSerializer, ToppingSerializer, OrderStatusSerializer
from .models import Order, PizzaBase, Cheese, Topping, OrderStatus

@api_view(['GET', 'POST'])
def apiOverview(request):
    api_urls = {
        'Create': '/orderApis/create/',
        'Update': '/orderApis/update/<int:order_id>/',
        'Status': '/orderApis/status/<int:order_id>/',
        'List': '/orderApis/list/',
    }

    return Response(api_urls)

@api_view(['GET'])
def orderList(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
