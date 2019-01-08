from django.conf.urls import url
from django.urls import path
from . import views

app_name = "report"

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^client$', views.register_client, name='register client'),
    # url(r'^registerUser$', views.register_user, name='register_user')
    path('weekly', views.weeklyReport, name='weekly_report'),
    path('monthly', views.monthlyReport, name='monthly_report'),
    path('annual', views.yearlyReport, name='annual_report'),
]