# deliverymen_intfc.py

from abc import ABC, abstractmethod

# Defining an abstract base class for deliverymen operations
class DeliverymenInterface(ABC):

    # Abstract method to add a new delivery person with necessary details
    @abstractmethod
    def add_delivery_person(self, employee_id, postal_code_id, availability=True, number_of_deliveries=0, last_delivery_time=None):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to remove a delivery person by employee ID
    @abstractmethod
    def remove_delivery_person(self, employee_id):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to update the availability status of a delivery person
    @abstractmethod
    def update_availability(self, employee_id, availability):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get details of a delivery person by employee ID
    @abstractmethod
    def get_delivery_person_by_id(self, employee_id):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get available delivery persons by region (postal code ID)
    @abstractmethod
    def get_available_deliverymen_by_region(self, postal_code_id):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to assign an order to a delivery person
    @abstractmethod
    def assign_order_to_delivery_person(self, order_id, employee_id):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to update the last delivery time for a delivery person
    @abstractmethod
    def update_last_delivery_time(self, employee_id):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get delivery statistics of all deliverymen
    @abstractmethod
    def get_deliverymen_statistics(self):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to find the first available delivery person for a given postal code
    @abstractmethod
    def find_available_delivery_person(self, postal_code_id):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to set a delivery person as unavailable for a specified delay
    @abstractmethod
    def set_unavailable(self, employee_id, delay_seconds=30):
        pass  # Placeholder indicating this method must be implemented in derived classes