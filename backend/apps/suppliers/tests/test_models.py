from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.suppliers.models import Supplier
from apps.users.models import User


class TestSupplier(TestCase):

    def test_create_supplier(self):
        """Tests model creation with valid data."""

        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'email': 'demo@demo.com', 'countries': ['GB', 'US'],
            'datatypes': ['GP', 'GC'], 'consent': True, 'certified': True
        }
        supplier = Supplier(**data)
        supplier.save()
        supplier.refresh_from_db()
        assert str(supplier) == "Supplier: Test Company, email: demo@demo.com."

    def test_create_supplier_with_missing_email(self):
        """Tests model creation with missing email address."""

        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'datatypes': ['GP', 'GC']
        }
        supplier = Supplier(**data)
        try:
            supplier.full_clean()
        except ValidationError as e:
            message = e.message_dict.get('email', None)
            self.assertEqual(message, ['This field cannot be blank.'])

        assert supplier.datatypes == ['GP', 'GC']

    def test_create_supplier_with_invalid_datatype(self):
        """Tests model creation with invalid datatypes."""

        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'datatypes': ['XY', ''], 'email': 'demo@demo.com'
        }
        supplier = Supplier(**data)
        try:
            supplier.full_clean()
        except ValidationError as e:
            self.assertIsNotNone(e.message_dict.get('datatypes'))
            message = e.message_dict.get('datatypes', None)
            assert message == [
                "Item 1 in the array did not validate: Value 'XY' is not a valid choice."]

    def test_create_supplier_with_missing_consent(self):
        """Tests model with missing consent."""

        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'datatypes': ['GP', 'GC'], 'certified': True
        }
        supplier = Supplier(**data)
        try:
            supplier.full_clean()
        except ValidationError as e:
            self.assertIsNotNone(e.message_dict.get('consent'))
            message = e.message_dict.get('consent', None)
            assert message == ['“None” value must be either True or False.']

    def test_create_supplier_with_created_by_user(self):
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'email': 'demo@demo.com', 'countries': ['GB', 'US'],
            'datatypes': ['GP', 'GC'], 'consent': True, 'certified': True,
            'created_by': 'demo@demo.com'
        }
        supplier = Supplier(**data)
        supplier.save()
        supplier.refresh_from_db()
        assert supplier.created_by == 'demo@demo.com'

    def test_datatypes_enum(self):
        geotagged_photos = Supplier.DATATYPES.get_value('geotagged_photos')
        assert geotagged_photos == 'GP'
