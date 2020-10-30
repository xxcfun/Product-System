from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from order import models
from order.models import Order


def order_all(request):
    order_list = models.Order.objects.filter(is_valid=True)
    paginator = Paginator(order_list, 10)
    page = request.GET.get('page')
    try:
        Order = paginator.page(page)
    except PageNotAnInteger:
        Order = paginator.page(1)
    except EmptyPage:
        Order = paginator.page(paginator.num_pages)

    return render(request, 'order.html', {
        'Order': Order
    })


def order_detail(request, pk):
    """将订单加入生产列表"""
    order = get_object_or_404(Order, pk=pk, is_valid=True)
    return render(request, 'order_detail.html', {
        'order': order
    })
