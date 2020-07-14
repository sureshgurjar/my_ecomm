from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):

   pdts = Product.objects.all()
   return render(request, 'index.html',{'pdts': pdts}) 

def product_detail(request, id):
   pdt = Product.objects.get(id = id)
   return render(request, 'product.html', {'pdt': pdt})
