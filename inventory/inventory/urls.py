from django.contrib import admin
from django.urls import path, include
from user.views import UserFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('report.urls')),
    path('', include('user.urls')),
    path('', UserFormView.as_view()),
    path('', include('transaction.urls')),
    # path('', include('warehouse.urls'))
]