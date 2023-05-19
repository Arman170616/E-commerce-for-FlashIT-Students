from django.urls import path

from .views import add_to_cart

app_name = 'order'

urlpatterns =[
    
    path('add_to_cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    
]