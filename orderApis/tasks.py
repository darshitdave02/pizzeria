# your_app/tasks.py

from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Order
from celery import current_task
from time import sleep

@shared_task
def update_order_status(order_id, start_time):
    order = Order.objects.get(id=order_id)
    current_time = timezone.now()
    
    if (current_time - start_time).total_seconds() >= 300:  # 5 minutes
        order.status = 'Delivered'
    elif (current_time - start_time).total_seconds() >= 180:  # 3 minutes
        order.status = 'Dispatched'
    elif (current_time - start_time).total_seconds() >= 120:  # 2 minutes
        order.status = 'Preparing'
    elif (current_time - start_time).total_seconds() >= 60:   # 1 minute
        order.status = 'Accepted'
    
    order.save()

    # Check if 5 minutes have passed, if not reschedule the task
    if (current_time - start_time).total_seconds() < 300:
        current_task.update_state(state='PROGRESS')
        sleep(60)  # Sleep for 1 minute
        update_order_status.apply_async(args=[order_id, start_time], countdown=0)  # Reschedule the task
