from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.models import User


class RegisterSupplierAPIViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.get(email='demo@demo.com')

    def get_response(self, data, authenticate=True):
        url = reverse('suppliers:register-supplier')
        if authenticate:
            self.client.login(username='demo@demo.com', password='demo')
        return self.client.post(url, data, format='json')

    def test_user_not_authenticated(self):
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'email': 'demo@demo.com', 'consent': True, 'certified': True,
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US']
        }
        response = self.get_response(data, authenticate=False)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() == {
            'detail': 'Authentication credentials were not provided.'}

    def test_create_supplier(self):
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'email': 'demo@demo.com', 'consent': True, 'certified': True,
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US'],
            'created_by': 'demo@demo.com'
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
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US'],
            'created_by': self.user.email
        }
        response = self.get_response(data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            'email': ['This field is required.'],
            'company_name': ['This field is required.'],
            'contact_name': ['This field is required.'],
        }

    def test_create_supplier_with_invalid_datatype(self):
        # missing email
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'consent': True, 'certified': True, 'email': 'demo@demo.com',
            'datatypes': ['XY'], 'countries': ['GB', 'IE', 'US'],
            'created_by': self.user.email
        }
        response = self.get_response(data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {'datatypes': {
            '0': ['"XY" is not a valid choice.']}}

    def test_create_supplier_with_invalid_country(self):
        """Test invalid country."""
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'consent': True, 'certified': True, 'email': 'demo@demo.com',
            'datatypes': ['GC'], 'countries': ['XY'],
            'created_by': self.user.email
        }
        response = self.get_response(data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {'countries': {
            '0': ['"XY" is not a valid choice.']}}

    def test_create_supplier_with_missing_consent(self):
        """Test missing consent.
        """
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'certified': True, 'email': 'demo@demo.com',
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US'],
            'created_by': self.user.email
        }
        response = self.get_response(data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {'consent': ['This field is required.']}

    def test_create_supplier_with_missing_certified(self):
        """Test missing consent.
        """
        data = {
            'company_name': 'Test Company', 'contact_name': 'Test Contact',
            'consent': True, 'email': 'demo@demo.com',
            'datatypes': ['GC'], 'countries': ['GB', 'IE', 'US'],
            'created_by': self.user.email
        }
        response = self.get_response(data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {'certified': ['This field is required.']}


class CountryListTest(APITestCase):

    def test_get_countries_authenticated(self):
        url = reverse('suppliers:countries-list')
        self.client.login(username='demo@demo.com', password='demo')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 249

    def test_get_countries_anonymous_user(self):
        url = reverse('suppliers:countries-list')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
