from django.shortcuts import render
from apps.suppliers.models import Supplier
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.suppliers.views.serializers import RegisterSupplierSerializer


class RegisterSupplierAPIView(CreateAPIView):

    permission_classes = [IsAuthenticated, ]
    serializer_class = RegisterSupplierSerializer
    queryset = Supplier.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
