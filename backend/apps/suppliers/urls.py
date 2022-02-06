from django.urls import path
from apps.suppliers.views.api import RegisterSupplierAPIView, CountryList
from django.views.decorators.cache import cache_page

app_name = 'suppliers'

ONE_MONTH = 60 * 60 * 24 * 30

urlpatterns = [
    path('register/', RegisterSupplierAPIView.as_view(),
         name="register-supplier"),
    path('countries/', cache_page(ONE_MONTH)
         (CountryList.as_view()), name="countries-list")
]
