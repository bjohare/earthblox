from django.urls import path
from apps.suppliers.views.api import RegisterSupplierAPIView, CountryList

app_name = 'suppliers'

urlpatterns = [
    path('register/', RegisterSupplierAPIView.as_view(),
         name="register-supplier"),
    path('countries/', CountryList.as_view(), name="countries-list")
]
