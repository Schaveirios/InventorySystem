from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/', include('report.urls')),
    path('transaction/', include('transaction.urls')),
    path('user/', include('user.urls')),
    path('warehouse/', include('warehouse.urls'))
]