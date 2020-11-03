from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from order.models import Order
from product.models import Product


def order_list(request):
    """所有生产订单"""
    order_list = Order.objects.all()
    print(order_list)
    return render(request, 'production_order.html', {
        'order_list': order_list
    })
