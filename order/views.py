from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from order import models
from order.models import Order


class OrderView(ListView):
    models = Order
    template_name = 'order.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(is_valid=True).order_by('deliver_time')


def order_detail(request, pk):
    """将订单加入生产列表"""
    order = get_object_or_404(Order, pk=pk, is_valid=True)
    return render(request, 'order_detail.html', {
        'order': order
    })
