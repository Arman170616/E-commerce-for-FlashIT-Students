from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category, ProductImages
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        return context


#function based view pk is primary key

# def product_detail(request, pk):
#     item = Product.objects.get(id=pk)
#     photos = ProductImages.objects.filter(product=item).order_by('-created')
#     context = {
#         'item': item
#     }
#     return render(request, 'store/product.html', context)
