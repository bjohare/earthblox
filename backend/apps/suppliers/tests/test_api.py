from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegisterSupplierAPIViewTest(APITestCase):

    def get_response(self, data, *args, **kwargs):
        url = reverse('suppliers:register-supplier')
        return self.client.post(url, data, format='json')

    def test_create_supplier(self):
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'email': 'demo@demo.com', 'consent': True, 'certified': True,
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US']
        }
        response = self.get_response(data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {"id": 1, "company_name": "Test Company",
                                   "contact_name": "Test Contact",
                                   "email": "demo@demo.com",
                                   "datatypes": ["GC"],
                                   "countries": ["GB", "IE", "US"],
                                   "consent": True, "certified": True}

    def test_create_supplier_with_missing_data(self):
        """Test for missing fields."""

        # missing company_name, contact_name, email
        data = {
            'consent': True, 'certified': True,
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US']
        }
        response = self.get_response(data)
        assert response.json() == {
            'email': ['This field is required.'],
            'company_name': ['This field is required.'],
            'contact_name': ['This field is required.']
        }

    def test_create_supplier_with_invalid_datatype(self):
        # missing email
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'consent': True, 'certified': True, 'email': 'demo@demo.com',
            'datatypes': ['XY'], 'countries': ['GB', 'IE', 'US']
        }
        response = self.get_response(data)
        assert response.json() == {'datatypes': {
            '0': ['"XY" is not a valid choice.']}}

    def test_create_supplier_with_invalid_country(self):
        """Test invalid country."""
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'consent': True, 'certified': True, 'email': 'demo@demo.com',
            'datatypes': ['GC'], 'countries': ['XY']
        }
        response = self.get_response(data)
        assert response.json() == {'countries': {
            '0': ['"XY" is not a valid choice.']}}

    def test_create_supplier_with_missing_consent(self):
        """Test missing consent.
        """
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'certified': True, 'email': 'demo@demo.com',
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US']
        }
        response = self.get_response(data)
        assert response.json() == {'consent': ['This field is required.']}

    def test_create_supplier_with_missing_certified(self):
        """Test missing consent.
        """
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'consent': True, 'email': 'demo@demo.com',
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US']
        }
        response = self.get_response(data)
        assert response.json() == {'certified': ['This field is required.']}
