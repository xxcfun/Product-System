import datetime
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView

from order.models import Order, OrderList


class OrderView(ListView):
    """订单列表 所有抓取的订单"""
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
    """完成订单"""
    template_name = 'order_finish.html'

    def get_queryset(self):
        return Order.objects.filter(order_status=5)


class OrderDeleteView(OrderView):
    """删除订单"""
    template_name = 'order_delete.html'

    def get_queryset(self):
        return Order.objects.filter(is_valid=False)


def order_finish(request):
    """函数视图"""
    return render(request, 'order_finish.html', {

    })


def order_del(request, order_id):
    """订单删除 逻辑删除"""
    order = get_object_or_404(Order, order_id=order_id, is_valid=True)
    order.is_valid = False
    order.save()
    return redirect('order')


def order_mine(request):
    """查看自己待生产的订单"""
    name = request.session.get('user_name')
    order_list = Order.objects.filter(salesperson=name, is_valid=True)
    return render(request, 'order.html', {
        'orders': order_list
    })


def order_mine_finish(request):
    """查看自己已完成的订单"""
    name = request.session.get('user_name')
    order_list = Order.objects.filter(salesperson=name, is_valid=True, order_status=5)
    return render(request, 'order_finish.html', {
        'orders': order_list
    })


def order_mine_delete(request):
    """查看自己已删除的订单"""
    name = request.session.get('user_name')
    order_list = Order.objects.filter(salesperson=name, is_valid=False)
    return render(request, 'order_delete.html', {
        'orders': order_list
    })
