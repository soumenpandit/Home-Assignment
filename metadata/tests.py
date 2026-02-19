from django.test import TestCase
from django.db import IntegrityError
from datetime import date
from rest_framework.test import APIClient
from .models import Customer, Order


class CustomerOrderAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_customer(self):
        response = self.client.post(
            "/api/customers/",
            {
                "name": "John Doe",
                "email": "john@example.com"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 1)

    def test_create_order_for_customer(self):
        customer = Customer.objects.create(
            name="Alice",
            email="alice@example.com"
        )

        response = self.client.post(
            f"/api/customers/{customer.id}/orders/",
            {
                "order_number": "ORD-001",
                "amount": "250.50"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.first().customer, customer)

    def test_create_customer_with_dob(self):
        response = self.client.post(
            "/api/customers/",
            {
                "name": "John Doe",
                "email": "john@example.com",
                "date_of_birth": "1990-05-20"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(
            Customer.objects.first().date_of_birth,
            date(1990, 5, 20)
        )

    def test_future_dob_not_allowed(self):
        response = self.client.post(
            "/api/customers/",
            {
                "name": "Future User",
                "email": "future@example.com",
                "date_of_birth": "2090-01-01"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

