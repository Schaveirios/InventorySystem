from django.conf.urls import url
from django.urls import path
from . import views

app_name = "warehouse"

urlpatterns = [
    path('', views.warehouse, name='inventory'),
    path('add_item/', views.add_item, name='add_new_item'),
]