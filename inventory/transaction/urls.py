from django.conf.urls import url
from django.urls import path
from . import views

app_name = "transact"

urlpatterns = [
    path('sold', views.sold_item, name='sold_item'),
    path('return', views.return_item, name='return_item'),
    path('searchPurchase', views.search_purchase, name='search_purchase'),
]
