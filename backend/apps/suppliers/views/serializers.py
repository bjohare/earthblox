from rest_framework.serializers import ModelSerializer
from django_countries.serializers import CountryFieldMixin
from rest_framework.serializers import CharField
from rest_framework.validators import UniqueValidator
from apps.suppliers.models import Supplier


class RegisterSupplierSerializer(CountryFieldMixin, ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['id', 'company_name', 'contact_name', 'email',
                  'datatypes', 'countries', 'consent', 'certified']

    company_name = CharField(
        validators=[UniqueValidator(queryset=Supplier.objects.all(
        ), message="A company with this name already exists.")]
    )
