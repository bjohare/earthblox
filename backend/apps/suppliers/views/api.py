from rest_framework.views import APIView
from apps.suppliers.models import Supplier
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.suppliers.views.serializers import RegisterSupplierSerializer
from django_countries.data import COUNTRIES


class RegisterSupplierAPIView(CreateAPIView):
    """API endpoint to register drone suppliers.
    """

    permission_classes = [IsAuthenticated, ]
    serializer_class = RegisterSupplierSerializer
    queryset = Supplier.objects.all()

    def perform_create(self, serializer):
        """Add user info to model.
        """
        email = self.request.user.email
        serializer.save(created_by=email, modified_by=email)


class CountryList(APIView):
    """API endpoint returning a list of countries.
    """
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format="json"):
        countries = [{'code': code,  'label': label}
                     for (code, label) in COUNTRIES.items()]
        return Response(countries)
