from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from product.models import Product


class ProdOrderView(ListView):
    """所有生产订单"""
    model = Product
    template_name = 'production_order.html'
    context_object_name = 'products'
    paginate_by = 10
