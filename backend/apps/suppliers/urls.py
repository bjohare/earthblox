from django.urls import path
from apps.suppliers.views.api import RegisterSupplierAPIView

app_name = 'suppliers'

urlpatterns = [
    path('register/', RegisterSupplierAPIView.as_view(),
         name="register-supplier")
]
