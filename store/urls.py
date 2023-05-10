from django.urls import path
from store.views import HomeListView, ProductDetailView


app_name = 'store'

urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_details'),


]