import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView

from order.models import Order, OrderList, OrderBill
from user.models import User
from utils import constants


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


def order_seach(request):
    """订单搜索"""
    if 'customer' in request.GET and request.GET['customer']:
        customer = request.GET['customer']
        order = Order.objects.filter(customer__icontains=customer).exclude(is_valid=False)
    elif 'status' in request.GET and request.GET['status']:
        status = request.GET['status']
        order = Order.objects.filter(order_status=status).exclude(is_valid=False)
    elif 'salesperson' in request.GET and request.GET['salesperson']:
        salesperson = request.GET['salesperson']
        order = Order.objects.filter(salesperson=salesperson).exclude(is_valid=False)
    else:
        order = Order.objects.exclude(is_valid=False)
    paginator = Paginator(order, 10)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    order_list = OrderList.objects.all()
    user_list = User.objects.filter(power=1)
    return render(request, 'order_seach.html', {
        'orders': orders,
        'order_list': order_list,
        'user_list': user_list
    })


class OrderBillView(ListView):
    """查询所有人的物流单号信息"""
    model = OrderBill
    template_name = 'order_bill.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        name = self.request.session.get('user_name')
        return OrderBill.objects.filter(order__salesperson=name, order__order_status=constants.ORDER_WC)


class OrderAllBillView(OrderBillView):
    """查看所有人的物流单号信息"""
    def get_queryset(self):
        return OrderBill.objects.filter(order__order_status=constants.ORDER_WC)


def order_odd(request, order_id):
    """物流填写"""
    odd_number = request.POST.get('odd_number')
    orderbill = get_object_or_404(OrderBill, order_id=order_id)
    orderbill.odd_number = odd_number
    orderbill.save()
    return redirect('order_bill')
