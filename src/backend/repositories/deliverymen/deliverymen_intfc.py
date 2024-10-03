# backend/repositories/deliverymen/deliverymen_intfc.py

from abc import ABC, abstractmethod

class DeliverymenInterface(ABC):

    @abstractmethod
    def add_delivery_person(self, employee_id, postal_code_id, availability=True, number_of_deliveries=0, last_delivery_time=None):
        pass

    @abstractmethod
    def remove_delivery_person(self, employee_id):
        pass

    @abstractmethod
    def update_availability(self, employee_id, availability):
        pass

    @abstractmethod
    def get_delivery_person_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_available_deliverymen_by_region(self, postal_code_id):
        pass

    @abstractmethod
    def assign_order_to_delivery_person(self, order_id, employee_id):
        pass

    @abstractmethod
    def update_last_delivery_time(self, employee_id):
        pass

    @abstractmethod
    def get_deliverymen_statistics(self):
        pass

    @abstractmethod
    def find_available_delivery_person(self, postal_code_id):
        pass

    @abstractmethod
    def set_unavailable(self, employee_id, delay_seconds=30):
        pass