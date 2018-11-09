from django.conf.urls import url
from django.urls import path
from . import views

app_name = "warehouse"

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^client$', views.register_client, name='register client'),
    # url(r'^registerUser$', views.register_user, name='register_user')
    path('', views.warehouse, name='inventory'),
    path('add_item/', views.add_item, name='add_new_item'),
]