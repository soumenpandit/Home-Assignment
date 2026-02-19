from django.urls import path
from .views import (
    CustomerListCreateView,
    CustomerRetrieveView,
    OrderListCreateView,
)

urlpatterns = [
    path("customers/", CustomerListCreateView.as_view()),
    path("customers/<int:pk>/", CustomerRetrieveView.as_view()),
    path("customers/<int:customer_id>/orders/", OrderListCreateView.as_view()),
]
