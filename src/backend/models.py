# models.py
from backend.database import connect_to_db
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
    def __init__(self, customer_id, items, total_price, status='Being Prepared'):
        self.order_id = None  # Устанавливается после сохранения в БД
        self.customer_id = customer_id
        self.items = items  # Список товаров: пиццы, напитки, десерты
        self.total_price = total_price
        self.status = status
        self.created_at = datetime.now()