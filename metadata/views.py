from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    """
    GET  -> List customers
    POST -> Create customer
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveView(generics.RetrieveAPIView):
    """
    GET -> Retrieve customer with orders
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    """
    GET  -> List orders for a customer
    POST -> Create order for a customer
    """
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(customer_id=self.kwargs["customer_id"])

    def perform_create(self, serializer):
        serializer.save(customer_id=self.kwargs["customer_id"])
