from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from product import models
from product.models import Product
from utils import constants


def prod(request):
    statusname = request.GET.get('status', '')
    prod_list = models.Product.objects.filter(is_valid=True)
    if statusname:
        prod_list = models.Product.objects.filter(is_valid=True, status=statusname)
    paginator = Paginator(prod_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'prod.html', {
        'constants': constants,
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


def edit(request, pk):
    prod = get_object_or_404(Product, pk=pk, is_valid=True)
    prod_status = prod.status
    if prod_status < 5:
        Product.objects.filter(pk=pk).update(status=prod_status+1)
    print(prod_status)
    return redirect('prod'+f'/?status={prod_status}')
