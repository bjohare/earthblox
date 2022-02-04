from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault
from django_countries.serializers import CountryFieldMixin
from apps.suppliers.models import Supplier


class RegisterSupplierSerializer(CountryFieldMixin, ModelSerializer):

    created_by = PrimaryKeyRelatedField(
        read_only=True, default=CurrentUserDefault())

    class Meta:
        model = Supplier
        fields = ['id', 'company_name', 'contact_name', 'email',
                  'datatypes', 'countries', 'consent', 'certified',
                  'created_by', 'modified_by']
