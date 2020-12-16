from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from order.models import Order, OrderBill
from order.views import OrderView
from product.models import Product
from utils import constants


class ProOrderView(OrderView):
    """抓取来的所有订单列表"""
    template_name = 'prod_order.html'

    def get_queryset(self):
        return Order.objects.filter(order_status=constants.ORDER_DSC, is_valid=True)


def order_detail(request, order_id):
    """订单列表详情，主要用来填写生产数量"""
    order = get_object_or_404(Order, order_id=order_id, is_valid=True)
    return render(request, 'prod_order_detail.html', {
        'order': order
    })


def prod_add(request, order_id):
    """将订单添加到生产控制中"""
    order = get_object_or_404(Order, order_id=order_id)
    order.order_status = constants.ORDER_SCZ
    order.save()
    return redirect('prod_produce')
    # order = get_object_or_404(Order, order_id=order_id)
    # user = get_object_or_404(User, name=request.session.get('user_name'))
    # # 拿到订单里的数量，先做判断
    # order_num = order.sumnumber
    # # 拿到要生产的数量
    # count = int(request.POST.get('owen_num'))
    # # 检验产品生产数量
    # if order_num < count:
    #     return HttpResponse('数量不合法')
    # # 更新数量信息
    # order.update_number(count)
    #
    # # 更新订单的状态信息
    # """业务拉取订单，开始生产时，该订单状态改为生产中"""
    # order.update_status_scz()
    #
    # # # 将数量为0的订单改为不启用状态
    # # if order.sumnumber == 0:
    # #     order.is_valid = False
    # #     order.save()
    #
    # # 生成生产信息记录
    # # 如果已经添加到生产列表中，只把生产数量更新就行
    # try:
    #     product = Product.objects.get(order=order, user=user, status=constants.ORDER_BLZ)
    #     count = product.owen_num + count
    #     product.owen_num = count
    #     product.save()
    # except Product.DoesNotExist:
    #     Product.objects.create(
    #         order=order,
    #         user=user,
    #         owen_num=count,
    #     )
    # return redirect('prod_material')


def prod_del(request, order_id):
    """将订单添加到生产控制中"""
    order = get_object_or_404(Order, order_id=order_id)
    order.is_valid = 0
    order.save()
    return redirect('prod_order')


class ProductStatusView(OrderView):
    """生产控制中的备料，生产，发货和订单完成"""
    models = Order
    template_name = 'prod_status.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        """添加上下文信息，将url拆分，拿到具体的每个状态"""
        context['url'] = self.request.get_full_path().split('/')[2]
        # 用get_full_path()来获取url地址，split分割url，然后取第三个字符串
        return context


class ProduceView(ProductStatusView):
    """生产中"""
    def get_queryset(self):
        # user = self.request.session.get('user_id')
        return Order.objects.filter(order_status=constants.ORDER_SCZ).order_by('-update_time')


class DeliverView(ProductStatusView):
    """待发货"""
    def get_queryset(self):
        # user = self.request.session.get('user_id')
        return Order.objects.filter(order_status=constants.ORDER_DFH).order_by('-update_time')


class FinishView(ProductStatusView):
    """订单完成"""
    def get_queryset(self):
        # user = self.request.session.get('user_id')
        return Order.objects.filter(order_status=constants.ORDER_WC).order_by('-update_time')


def prod_edit(request, order_id):
    """状态修改"""
    order = get_object_or_404(Order, order_id=order_id)
    order_status = order.order_status
    # 生产中-待发货，只有所有订单都生产完毕才能点发货
    if order_status == constants.ORDER_SCZ:
        order.order_status = constants.ORDER_DFH
        order.save()
        return redirect('prod_deliver')
    # 待发货-订单完成
    if order_status == constants.ORDER_DFH:
        order.order_status = constants.ORDER_WC
        order.save()
        # 订单发货后，将完成的订单存入order_bill表
        orderbill = OrderBill
        orderbill.objects.get_or_create(order_id=order.order_id)
        return redirect('prod_finish')


"""批量操作"""
def prod_del_all(request):
    """批量删除订单信息"""
    if request.method == 'POST':
        # 得到要删除的id列表
        values = request.POST.getlist('vals')
        for i in values:
            # 如果i不为空，就获取这个字段
            if i != '':
                order = get_object_or_404(Order, order_id=i)
                order.is_valid = 0
                order.save()
    return redirect('prod_order')


def prod_add_all(request):
    """批量生产订单"""
    if request.method == 'POST':
        values = request.POST.getlist('vals')
        for i in values:
            if i != '':
                order = get_object_or_404(Order, order_id=i)
                order.order_status = constants.ORDER_SCZ
                order.save()
    return redirect('prod_produce')


def prod_edit_all(request):
    """批量更改订单状态"""
    if request.method == 'POST':
        values = request.POST.getlist('vals')
        for i in values:
            if i != '':
                order = get_object_or_404(Order, order_id=i)
                order_status = order.order_status
                if order_status == constants.ORDER_SCZ:
                    order.order_status = constants.ORDER_DFH
                    order.save()
                if order_status == constants.ORDER_DFH:
                    order.order_status = constants.ORDER_WC
                    order.save()
                    orderbill = OrderBill
                    orderbill.objects.get_or_create(order_id=order.order_id)
        return HttpResponse('ok')

