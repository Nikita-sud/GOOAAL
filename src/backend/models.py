# models.py

from datetime import datetime

# Defining the Customer class to represent a customer entity
class Customer:
    def __init__(self, name, last_name, gender_id, birthdate, phone, address_id):
        self.customer_id = None  # Set after saving to the database
        self.name = name  # Customer's first name
        self.last_name = last_name  # Customer's last name
        self.gender_id = gender_id  # ID representing the gender of the customer
        self.birthdate = birthdate  # Date of birth of the customer
        self.phone = phone  # Phone number of the customer
        self.address_id = address_id  # Address ID associated with the customer
        self.number_orders = 0  # Number of orders placed by the customer

# Defining the Order class to represent an order entity
class Order:
    def __init__(self, customer_id, items, total_price, discount_applied, status_id=1, created_at=None):
        self.customer_id = customer_id  # ID of the customer who placed the order
        self.items = items  # List of items in the order
        self.total_price = total_price  # Total price of the order
        self.status_id = status_id  # Status ID of the order (default is 1, e.g., "Being Prepared")
        self.created_at = created_at or datetime.now()  # Creation timestamp (default is current time)
        self.order_id = None  # Set after saving to the database
        self.discount_applied = discount_applied  # Discount applied to the order

# Defining the DeliveryPerson class to represent a delivery person entity
class DeliveryPerson:
    def __init__(self, employee_id, postal_code_id, availability=True, number_of_deliveries=0, last_delivery_time=None):
        self.employee_id = employee_id  # Employee ID of the delivery person
        self.postal_code_id = postal_code_id  # Postal code ID where the delivery person operates
        self.availability = availability  # Availability status of the delivery person
        self.number_of_deliveries = number_of_deliveries  # Number of deliveries completed by the delivery person
        self.last_delivery_time = last_delivery_time  # Timestamp of the last delivery made