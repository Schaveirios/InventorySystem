from django.conf.urls import url
from user import views
from django.urls import path
from . import views

app_name = 'user'

urlpatterns=[
    path('',views.index,name='index'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('special/',views.special,name='special'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
]