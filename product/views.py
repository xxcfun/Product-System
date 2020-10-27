from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from product import models
from product.models import Product
from utils import constants


def prod_all(request):
    prod_list = models.Product.objects.filter(is_valid=True)
    paginator = Paginator(prod_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'prod.html', {
        'products': products
    })


def prod_bl(request):
    prod_bl_list = models.Product.objects.filter(is_valid=True, status=constants.PROD_BL)
    paginator = Paginator(prod_bl_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'prod.html', {
        'products': products
    })


def prod_pd(request):
    prod_pd_list = models.Product.objects.filter(is_valid=True, status=constants.PROD_PD)
    paginator = Paginator(prod_pd_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'prod.html', {
        'products': products
    })


def prod_scz(request):
    prod_scz_list = models.Product.objects.filter(is_valid=True, status=constants.PROD_SC)
    paginator = Paginator(prod_scz_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'prod.html', {
        'products': products
    })


def prod_dfh(request):
    prod_dfh_list = models.Product.objects.filter(is_valid=True, status=constants.PROD_DFH)
    paginator = Paginator(prod_dfh_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'prod.html', {
        'products': products
    })


def prod_ddwc(request):
    prod_ddwc_list = models.Product.objects.filter(is_valid=True, status=constants.PROD_WC)
    paginator = Paginator(prod_ddwc_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'prod.html', {
        'products': products
    })


def seach(request):
    return render(request, 'prod_seach.html', {

    })


class ProdListView(ListView):
    models = Product
    template_name = 'prod_list.html'
    context_object_name = 'prod_list'
    paginate_by = 10

    def get_queryset(self):
        return models.Product.objects.filter(~Q(status=constants.PROD_WC))


def prod_edit(request, pk):
    prod = get_object_or_404(Product, pk=pk, is_valid=True)
    prod_status = prod.status
    if prod_status == 1:
        Product.objects.filter(pk=pk).update(status=2)
        return redirect('prod_pd')
    if prod_status == 2:
        Product.objects.filter(pk=pk).update(status=3)
        return redirect('prod_scz')
    if prod_status == 3:
        Product.objects.filter(pk=pk).update(status=4)
        return redirect('prod_dfh')
    if prod_status == 4:
        Product.objects.filter(pk=pk).update(status=5)
        return redirect('prod_ddwc')


def prod_del(request, pk):
    Product.objects.filter(pk=pk).update(is_valid=False)
    return redirect('prod_ddwc')
