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
        # 添加额外的上下文信息，将配件加入订单中
        kwargs['order_list'] = OrderList.objects.all()
        return super(OrderView, self).get_context_data(**kwargs)

    def get_queryset(self):
        # 返回个人的订单
        name = self.request.session.get('user_name')
        # return Order.objects.filter(is_valid=True).exclude(order_status=4)
        return Order.objects.filter(is_valid=True, salesperson=name).exclude(order_status=4)


class OrderFinishView(OrderView):
    """完成订单"""
    template_name = 'order_finish.html'

    def get_queryset(self):
        name = self.request.session.get('user_name')
        return Order.objects.filter(order_status=4, salesperson=name)


class OrderDeleteView(OrderView):
    """删除订单"""
    template_name = 'order_delete.html'

    def get_queryset(self):
        name = self.request.session.get('user_name')
        return Order.objects.filter(is_valid=False, salesperson=name)


# def order_del(request, order_id):
#     """订单删除 逻辑删除"""
#     order = get_object_or_404(Order, order_id=order_id, is_valid=True)
#     order.is_valid = False
#     order.save()
#     return redirect('order')


class OrderAllView(OrderView):
    """查看所有待生产的订单"""
    def get_queryset(self):
        return Order.objects.filter(is_valid=True).exclude(order_status=4)


class OrderAllFinishView(OrderFinishView):
    """查看所有已完成的订单"""
    def get_queryset(self):
        return Order.objects.filter(is_valid=True, order_status=4)


class OrderAllDeleteView(OrderDeleteView):
    """查看自己已删除的订单"""
    def get_queryset(self):
        return Order.objects.filter(is_valid=False)
