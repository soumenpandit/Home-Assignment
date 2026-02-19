# Data Structure Management Service

## Description
REST API to manage datasets and their metadata fields.

## Tech Stack
- Python
- Django + DRF
- SQLite
- Django ORM

## Features
- Create & list datasets
- Add & list data elements
- DB-level constraints
- API tests included

## Run Project
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Overview

This project is a simple backend service built with Python, Django, and Django REST Framework.
It manages core business entities such as Customers and Orders, allowing clients to create and retrieve customers, place orders for customers, and query customers along with their orders.

The project focuses on clean data modeling, database integrity, and testable REST APIs.

Data Model & Design Decisions
Customer

The Customer model represents an end user or client of the system.

Fields:

name – Customer’s full name

email – Unique email identifier

date_of_birth – Optional date of birth

created_at – Timestamp when the record was created

Design decisions:

Email is enforced as unique and used as a natural identifier.

date_of_birth is optional to allow partial customer records.

Timestamps are included for audit and traceability.

Order

The Order model represents a transaction placed by a customer.

Fields:

customer – Foreign key reference to Customer

order_number – Unique business identifier for the order

amount – Monetary value of the order

created_at – Timestamp when the order was created

Design decisions:

A one-to-many relationship is used: one customer can have multiple orders.

Orders cannot exist without a customer.

Monetary values use DecimalField to avoid floating-point precision issues.

Order numbers are unique to prevent duplication.

Database Constraints

The following constraints are enforced at the database level:

Unique customer email – prevents duplicate customer records.

Unique order number – ensures each order is uniquely identifiable.

Foreign key constraint – orders must belong to a valid customer.

Cascade delete – deleting a customer deletes all associated orders.

These constraints ensure strong data integrity even if validations are bypassed at the API level.

Validation Strategy

Validation is applied at multiple layers:

Serializer-Level Validation

Ensures required fields are present.

Prevents invalid input (e.g., future date of birth).

Ensures order amounts are valid.

Database-Level Validation

Enforces uniqueness and referential integrity.

Acts as the final safeguard for business rules.

View-Level Control

Customer–order relationships are derived from the URL path rather than request data.

Prevents clients from manipulating foreign key relationships.

Assumptions & Trade-Offs
Assumptions

Email uniquely identifies a customer.

Orders are always created in the context of an existing customer.

Authentication and authorization are out of scope for this implementation.

Trade-Offs

SQLite is used for simplicity instead of a production database.

The system does not support order updates or deletions to keep scope minimal.

Advanced features such as pagination, filtering, and authentication are intentionally excluded.

API Endpoints
Customers

POST /api/customers/ – Create a customer

GET /api/customers/ – List all customers

GET /api/customers/{id}/ – Retrieve a customer with orders

Orders

POST /api/customers/{customer_id}/orders/ – Create an order for a customer

GET /api/customers/{customer_id}/orders/ – List orders for a customer

########  How to Run the Application   ############
1. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

2. Install Dependencies
pip install -r requirements.txt

3. Run Migrations

python manage.py makemigrations
python manage.py migrate

4. Start Development Server

python manage.py runserver

5. Run All Tests
python manage.py test metadata

