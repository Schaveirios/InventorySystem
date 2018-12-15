from django.conf.urls import url
from user import views
from django.urls import path
from . import views
# SET THE NAMESPACE!
app_name = 'user'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
]