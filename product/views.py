import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from order.models import Order
from product.models import Product
from user.models import User
from utils import constants


class OrderView(ListView):
    """抓取来的所有订单列表"""
    models = Order
    template_name = 'prod_order.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        now_day = datetime.datetime.now().date()
        return Order.objects.filter(is_valid=True, created_time=now_day).order_by('deliver_time')


def order_detail(request, pk):
    """订单列表详情，主要用来填写生产数量"""
    order = get_object_or_404(Order, pk=pk, is_valid=True)
    return render(request, 'prod_order_detail.html', {
        'order': order
    })


def prod_add(request, pk):
    """将订单添加到生产控制中"""
    order = get_object_or_404(Order, pk=pk)
    user = get_object_or_404(User, name=request.session.get('user_name'))
    # 拿到订单里的数量，先做判断
    order_num = order.sumnumber
    # 拿到要生产的数量
    count = int(request.POST.get('owen_num'))
    # 检验产品生产数量
    if order_num < count:
        return HttpResponse('数量不合法')
    # 更新数量信息
    order.update_number(count)

    # 将数量为0的订单改为不启用状态
    if order.sumnumber == 0:
        order.is_valid = False
        order.save()

    # 生成生产信息记录
    # 如果已经添加到生产列表中，只把生产数量更新就行
    try:
        product = Product.objects.get(order=order, user=user, status=constants.PROD_BL)
        count = product.owen_num + count
        product.owen_num = count
        product.save()
    except Product.DoesNotExist:
        Product.objects.create(
            order=order,
            user=user,
            owen_num=count,
        )
    return redirect('prod_material')


"""
    这里主要是流程控制
"""
class ProductStatusView(ListView):
    """生产控制中的备料，生产，发货和订单完成"""
    models = Product
    template_name = 'prod_status.html'
    context_object_name = 'product_list'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        """添加上下文信息，将url拆分，拿到具体的每个状态"""
        context['url'] = self.request.get_full_path().split('/')[2]
        # 用get_full_path()来获取url地址，split分割url，然后取第三个字符串
        return context


class MaterialView(ProductStatusView):
    """备料"""
    def get_queryset(self):
        user = self.request.session.get('user_id')
        return Product.objects.filter(status=constants.PROD_BL, user=user).order_by('-updated_time')


class ProduceView(ProductStatusView):
    """生产中"""
    def get_queryset(self):
        user = self.request.session.get('user_id')
        return Product.objects.filter(status=constants.PROD_SC, user=user).order_by('-updated_time')


class DeliverView(ProductStatusView):
    """待发货"""
    def get_queryset(self):
        user = self.request.session.get('user_id')
        return Product.objects.filter(status=constants.PROD_DFH, user=user).order_by('-updated_time')


class FinishView(ProductStatusView):
    """订单完成"""
    def get_queryset(self):
        user = self.request.session.get('user_id')
        return Product.objects.filter(status=constants.PROD_WC, user=user).order_by('-updated_time')


def prod_edit(request, pk):
    """状态修改"""
    prod = get_object_or_404(Product, pk=pk)
    prod_status = prod.status
    if prod_status == constants.PROD_BL:
        prod.status = constants.PROD_SC
        prod.save()
        return redirect('prod_produce')
    if prod_status == constants.PROD_SC:
        prod.status = constants.PROD_DFH
        prod.save()
        return redirect('prod_deliver')
    if prod_status == constants.PROD_DFH:
        prod.status = constants.PROD_WC
        prod.save()
        return redirect('prod_finish')
"""
    流程控制结束
"""


def prod_seach(request):
    # 订单筛选搜索
    customer = request.POST.get('customer', '')
    good = request.POST.get('good', '')
    status = request.POST.get('status', '')
    if customer:
        products = Product.order.objects.filter(customer__name=customer)
    products = Product.objects.all()
    return render(request, 'prod_seach.html', {
        'products': products
    })
