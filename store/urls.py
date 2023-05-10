from django.urls import path
from store.views import HomeListView


urlpatterns = [
    path('', HomeListView.as_view(), name='index'),


]