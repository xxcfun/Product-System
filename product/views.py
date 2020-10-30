from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from order.models import Order
from product import models
from product.models import Product
from user.models import User
from utils import constants


def product_all(request):
    """所有待生产订单"""
    user = get_object_or_404(User, name=request.session.get('user_name'))
    product_list = user.products.filter(status=constants.PROD_BL)
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    try:
        Product = paginator.page(page)
    except PageNotAnInteger:
        Product = paginator.page(1)
    except EmptyPage:
        Product = paginator.page(paginator.num_pages)

    return render(request, 'product.html', {
        'Product': Product
    })


def prod_add(request, pk):
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
    return HttpResponse('ok')


class ProductStatusView(ListView):
    models = Product
    template_name = 'product_status.html'
    context_object_name = 'products'


class BLView(ProductStatusView):
    def get_queryset(self):
        return Product.objects.filter(status=constants.PROD_BL)


class SCZView(ProductStatusView):
    def get_queryset(self):
        return Product.objects.filter(status=constants.PROD_SC)


class DFHView(ProductStatusView):
    def get_queryset(self):
        return Product.objects.filter(status=constants.PROD_DFH)


class DDWCView(ProductStatusView):
    def get_queryset(self):
        return Product.objects.filter(status=constants.PROD_WC)


def product_seach(request):
    # 所有订单

    return render(request, 'prod_seach.html', {

    })

# def prod_bl(request):
#     prod_bl_list = models.ProductList.objects.filter(is_valid=True, status=constants.PROD_BL)
#     paginator = Paginator(prod_bl_list, 10)
#     page = request.GET.get('page')
#     try:
#         ProductLists = paginator.page(page)
#     except PageNotAnInteger:
#         ProductLists = paginator.page(1)
#     except EmptyPage:
#         ProductLists = paginator.page(paginator.num_pages)
#
#     return render(request, 'product.html', {
#         'ProductLists': ProductLists
#     })
#
#
# def prod_scz(request):
#     prod_scz_list = models.ProductList.objects.filter(is_valid=True, status=constants.PROD_SC)
#     paginator = Paginator(prod_scz_list, 10)
#     page = request.GET.get('page')
#     try:
#         ProductLists = paginator.page(page)
#     except PageNotAnInteger:
#         ProductLists = paginator.page(1)
#     except EmptyPage:
#         ProductLists = paginator.page(paginator.num_pages)
#
#     return render(request, 'product.html', {
#         'ProductLists': ProductLists
#     })
#
#
# def prod_dfh(request):
#     prod_dfh_list = models.ProductList.objects.filter(is_valid=True, status=constants.PROD_DFH)
#     paginator = Paginator(prod_dfh_list, 10)
#     page = request.GET.get('page')
#     try:
#         ProductLists = paginator.page(page)
#     except PageNotAnInteger:
#         ProductLists = paginator.page(1)
#     except EmptyPage:
#         ProductLists = paginator.page(paginator.num_pages)
#
#     return render(request, 'product.html', {
#         'ProductLists': ProductLists
#     })
#
#
# def prod_ddwc(request):
#     prod_ddwc_list = models.ProductList.objects.filter(is_valid=True, status=constants.PROD_WC)
#     paginator = Paginator(prod_ddwc_list, 10)
#     page = request.GET.get('page')
#     try:
#         ProductLists = paginator.page(page)
#     except PageNotAnInteger:
#         ProductLists = paginator.page(1)
#     except EmptyPage:
#         ProductLists = paginator.page(paginator.num_pages)
#
#     return render(request, 'product.html', {
#         'ProductLists': ProductLists
#     })
#
#
# def seach(request):
#     return render(request, 'prod_seach.html', {
#
#     })
#
#
# class ProdListView(ListView):
#     models = ProductList
#     template_name = 'order.html'
#     context_object_name = 'prod_list'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return models.ProductList.objects.filter(~Q(status=constants.PROD_WC))
#
#
# def prod_edit(request, pk):
#     prod = get_object_or_404(ProductList, pk=pk, is_valid=True)
#     prod_status = prod.status
#     if prod_status == 1:
#         ProductList.objects.filter(pk=pk).update(status=2)
#         return redirect('prod_pd')
#     if prod_status == 2:
#         ProductList.objects.filter(pk=pk).update(status=3)
#         return redirect('prod_scz')
#     if prod_status == 3:
#         ProductList.objects.filter(pk=pk).update(status=4)
#         return redirect('prod_dfh')
#     if prod_status == 4:
#         ProductList.objects.filter(pk=pk).update(status=5)
#         return redirect('prod_ddwc')
#
#
# def prod_del(request, pk):
#     ProductList.objects.filter(pk=pk).update(is_valid=False)
#     return redirect('prod_ddwc')
