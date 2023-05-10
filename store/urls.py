from django.urls import path
from store.views import HomeListView, ProductDetailView


urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),


]