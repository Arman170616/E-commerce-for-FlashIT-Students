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