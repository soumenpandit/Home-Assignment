from rest_framework import serializers
from .models import Customer, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "order_number", "amount", "customer", "created_at")
        read_only_fields = ("customer",)


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ("id", "name", "email", "date_of_birth",  "created_at", "orders")

    def validate_date_of_birth(self, value):
        if value and value >= value.today():
            raise serializers.ValidationError(
                "Date of birth must be in the past"
            )
        return value
