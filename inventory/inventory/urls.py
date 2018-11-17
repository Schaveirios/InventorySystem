from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('warehouse/',include('warehouse.urls')),
    path('transaction/',include('transaction.urls')),
]