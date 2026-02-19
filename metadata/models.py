from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataElement(models.Model):
    DATA_TYPES = [
        ("string", "String"),
        ("integer", "Integer"),
        ("boolean", "Boolean"),
        ("date", "Date"),
    ]

    dataset = models.ForeignKey(
        Dataset,
        related_name="elements",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=20, choices=DATA_TYPES)
    is_pii = models.BooleanField(default=False)

    class Meta:
        unique_together = ("dataset", "name")

    def __str__(self):
        return f"{self.dataset.name}.{self.name}"


class Customer(models.Model):
    """
    Business entity: Customer
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                name="unique_customer_email"
            )
        ]
    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Business entity: Order
    """
    customer = models.ForeignKey(
        Customer,
        related_name="orders",
        on_delete=models.CASCADE
    )
    order_number = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number


