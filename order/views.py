import datetime
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView

from order.models import Order, OrderList


# 原来订单列表
class OrderView(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['order_list'] = OrderList.objects.all()
        return super(OrderView, self).get_context_data(**kwargs)

    def get_queryset(self):
        now_day = datetime.datetime.now().date()
        return Order.objects.filter(created_time=now_day, is_valid=True)
        # return Order.objects.all()


class OrderFinishView(OrderView):
    # 原来订单完成列表
    template_name = 'order_finish.html'

    def get_queryset(self):
        now_day = datetime.datetime.now().date()
        return Order.objects.filter(created_time=now_day, is_valid=False)


def order_finish(request):
    """函数视图"""
    
    return render(request, 'order_finish.html', {

    })


def order_del(request, pk):
    """订单删除 逻辑删除"""
    order = get_object_or_404(Order, pk=pk, is_valid=True)
    order.is_valid = False
    order.save()
    return redirect('order_list')


def order_mine(request):
    now_day = datetime.datetime.now().date()
    name = request.session.get('user_name')
    order_list = Order.objects.filter(salesperson=name, created_time=now_day, is_valid=True)
    return render(request, 'order.html', {
        'order_list': order_list
    })
