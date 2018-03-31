from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, DeleteView
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
        goods = Goods.objects.filter(supplier=request.user)
        return render(request, self.template_name, locals())

class SupplierGoodsCreateView(CreateView):
    template_name = 'supplier_pages/create_goods.html'
    model = Goods
    fields = '__all__'
    success_url = '../../goods/'

