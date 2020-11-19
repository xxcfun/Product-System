import datetime
from django.shortcuts import render, get_object_or_404, redirect

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
        return Order.objects.filter(created_time=now_day, is_valid=True)


class OrderFinishView(OrderListView):
    template_name = 'production_finish.html'
    def get_queryset(self):
        now_day = datetime.datetime.now().date()
        return Order.objects.filter(created_time=now_day, is_valid=False)


def order_del(request, pk):
    order = get_object_or_404(Order, pk=pk, is_valid=True)
    order.is_valid = False
    order.save()
    return redirect('order_list')


def order_mine(request):
    now_day = datetime.datetime.now().date()
    name = request.session.get('user_name')
    order_list = Order.objects.filter(salesperson=name, created_time=now_day, is_valid=True)
    return render(request, 'production_order.html', {
        'order_list': order_list
    })
