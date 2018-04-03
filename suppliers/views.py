from django.shortcuts import render, render_to_response
from django.views.generic import View, UpdateView, CreateView, DeleteView
from django.shortcuts import redirect
from .models import Goods
from django.contrib.auth.models import User
from access.models import UserProfile
# Create your views here.


class SupplierHomePage(View):
    template_name = 'supplier_pages/supplier_home.html'

    def get(self, request):
        return render(request, self.template_name, locals())


class SuppliersGoodsView(View):
    template_name = 'supplier_pages/list_goods.html'

    def get(self, request):
        template = self.template_name
        goods = Goods.objects.filter(supplier=request.user)
        if request.is_ajax():
            try:
                if request.GET['data'] == 'get_page':
                    return render_to_response(template, locals())
            except KeyError:
                ''''''



class SupplierGoodsCreateView(CreateView):
    template_name = 'supplier_pages/create_goods.html'
    model = Goods
    fields = '__all__'
    success_url = '../../goods/'


class SupplierGoodsUpdateView(UpdateView):
    template_name = 'supplier_pages/update_goods.html'
    model = Goods
    success_url = '../../../goods/'
    fields = '__all__'


class SupplierGoodsDeleteView(DeleteView):
    template_name = 'supplier_pages/delete_goods.html'
    model = Goods
    success_url = '../../../goods/'
    fields = '__all__'
