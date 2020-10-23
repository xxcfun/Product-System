from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from product.models import Product


class ProdView(ListView):
    """订单生产流程"""
    model = Product
    template_name = 'prod.html'
    context_object_name = 'products'
    paginate_by = 10

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.erros, status=400)
        else:
            return response


class ProdListView(ProdView):
    """订单信息列表"""
    queryset = Product.objects.filter(deliver=False)
    template_name = 'prod_list.html'


class ProdSeachView(ProdView):
    """订单信息查询"""
    template_name = 'prod_seach.html'
