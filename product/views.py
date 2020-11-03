from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from order.models import Order
from product.models import Product
from user.models import User
from utils import constants


class ProdView(ListView):
    """所有生产订单"""
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    paginate_by = 10


def prod_add(request, pk):
    """将订单添加到生产控制中"""
    order = get_object_or_404(Order, pk=pk)
    user = get_object_or_404(User, name=request.session.get('user_name'))
    # 拿到订单里的数量，先做判断
    order_num = order.number
    # 拿到要生产的数量
    count = int(request.POST.get('owen_num'))
    # 检验产品生产数量
    if order_num < count:
        return HttpResponse('数量不合法')
    # 更新数量信息
    order.update_number(count)

    # 将数量为0的订单改为不启用状态
    if order.number == 0:
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
    return redirect('product_bl')


class ProductStatusView(ListView):
    """生产控制中的备料，生产，发货和订单完成"""
    models = Product
    template_name = 'product_status.html'
    context_object_name = 'products'
    paginate_by = 10


class BLView(ProductStatusView):
    """备料"""
    def get_queryset(self):
        user = self.request.session.get('user_id')
        return Product.objects.filter(status=constants.PROD_BL, user=user).order_by('-updated_time')


class SCZView(ProductStatusView):
    """生产中"""
    def get_queryset(self):
        user = self.request.session.get('user_id')
        return Product.objects.filter(status=constants.PROD_SC, user=user).order_by('-updated_time')


class DFHView(ProductStatusView):
    """待发货"""
    def get_queryset(self):
        user = self.request.session.get('user_id')
        return Product.objects.filter(status=constants.PROD_DFH, user=user).order_by('-updated_time')


class DDWCView(ProductStatusView):
    """订单完成"""
    def get_queryset(self):
        user = self.request.session.get('user_id')
        return Product.objects.filter(status=constants.PROD_WC, user=user).order_by('-updated_time')


def product_edit(request, pk):
    """状态修改"""
    prod = get_object_or_404(Product, pk=pk)
    prod_status = prod.status
    if prod_status == constants.PROD_BL:
        prod.status = constants.PROD_SC
        prod.save()
        return redirect('product_scz')
    if prod_status == constants.PROD_SC:
        prod.status = constants.PROD_DFH
        prod.save()
        return redirect('product_dfh')
    if prod_status == constants.PROD_DFH:
        prod.status = constants.PROD_WC
        prod.save()
        return redirect('product_ddwc')


def product_seach(request):
    # 订单筛选搜索
    products = Product.objects.all()
    return render(request, 'prod_seach.html', {
        'products': products
    })
