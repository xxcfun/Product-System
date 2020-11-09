import datetime
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from order.models import Order


class OrderListView(ListView):
    model = Order
    template_name = 'production_order.html'
    context_object_name = 'order_list'
    paginate_by = 10

    def get_queryset(self):
        now_day = datetime.datetime.now().date()
        return Order.objects.filter(created_time=now_day)

# def order_list(request):
#     """所有生产订单"""
#     now_day = datetime.datetime.now().date()
#     order_list = Order.objects.filter(created_time=now_day)
#     return render(request, 'production_order.html', {
#         'order_list': order_list
#     })
