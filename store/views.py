from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
# Create your views here.


# def home(request):
#     return render(request, 'store/index.html')

class HomeListView(ListView):
   model = Product
   template_name = 'store/index.html'
   context_object_name = 'products'




class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'item'


#fucltion based view pk is primary key
# def product_detail(request, pk):
#     item = Product.objects.get(id=pk)
#     context = {
#         'item': item
#     }
#     return render(request, 'store/product.html', context)
