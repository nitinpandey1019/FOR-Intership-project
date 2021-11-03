from django.shortcuts import render
from .models import Productmodel
from django.http import HttpResponse
from django.views import View
# Create your views here.

class Products(View):
    def get(self,request):
        productdata=Productmodel.objects.all()
        return render(request,'products/products.html',{'data':productdata})