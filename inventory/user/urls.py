from django.conf.urls import url
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]