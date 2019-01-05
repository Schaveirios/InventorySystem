from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from user import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    url(r'^special/',views.special,name='special'),
    path('user/',include('user.urls')),
    path('warehouse/',include('warehouse.urls')),
    path('logout', views.user_logout, name='logout'),
    path('transaction/',include('transaction.urls')),
]