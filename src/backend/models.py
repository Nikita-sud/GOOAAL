# models.py
from datetime import datetime

class Customer:
    def __init__(self, name, last_name, gender_id, birthdate, phone, address_id):
        self.customer_id = None  # Устанавливается после сохранения в БД
        self.name = name
        self.last_name = last_name
        self.gender_id = gender_id
        self.birthdate = birthdate
        self.phone = phone
        self.address_id = address_id
        self.number_orders = 0

class Order:
    def __init__(self, customer_id, items, total_price, discount_applied, status_id=1, created_at=None):
        self.customer_id = customer_id
        self.items = items
        self.total_price = total_price
        self.status_id = status_id
        self.created_at = created_at or datetime.now()
        self.order_id = None
        self.discount_applied = discount_applied

class DeliveryPerson:
    def __init__(self, employee_id, postal_code_id, availability=True, number_of_deliveries=0, last_delivery_time=None):
        self.employee_id = employee_id
        self.postal_code_id = postal_code_id
        self.availability = availability
        self.number_of_deliveries = number_of_deliveries
        self.last_delivery_time = last_delivery_time