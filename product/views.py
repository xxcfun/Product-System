from django.shortcuts import render, redirect, get_object_or_404

def product_all(request):
    """提起订单，开始生产"""

    return render(request, 'product.html', {

    })


def production(request, pk):
    return render(request, 'product.html', {

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
