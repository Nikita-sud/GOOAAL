# customer_intfc.py
from abc import ABC, abstractmethod

# Defining an abstract base class for customer operations
class CustomerInterface(ABC):

    # Abstract method to create a new user with necessary details
    @abstractmethod
    def create_user(self, name: str, last_name: str, gender: int, birthdate: str, phone: int, address: int):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get customer details by customer ID
    @abstractmethod
    def get_customer_by_id(self, id: int):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to delete a customer by customer ID
    @abstractmethod
    def delete_customer(self, customer_id: int):
        pass  # Placeholder indicating this method must be implemented in derived classes