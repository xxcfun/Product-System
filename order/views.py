from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from order import models


def order_all(request):
    order_list = models.Order.objects.filter(is_valid=True)
    paginator = Paginator(order_list, 10)
    page = request.GET.get('page')
    try:
        Order = paginator.page(page)
    except PageNotAnInteger:
        Order = paginator.page(1)
    except EmptyPage:
        Order = paginator.page(paginator.num_pages)

    return render(request, 'order.html', {
        'Order': Order
    })