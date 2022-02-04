from django.shortcuts import render
from apps.suppliers.models import Supplier
from rest_framework.generics import CreateAPIView
from apps.suppliers.views.serializers import RegisterSupplierSerializer


class RegisterSupplierAPIView(CreateAPIView):

    serializer_class = RegisterSupplierSerializer
    queryset = Supplier.objects.all()
