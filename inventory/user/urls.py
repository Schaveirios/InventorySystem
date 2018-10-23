from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "user"

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^client$', views.register_client, name='register client'),
    # url(r'^registerUser$', views.register_user, name='register_user')
    path('login/', TemplateView.as_view(template_name="login.html")),
]