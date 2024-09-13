from abc import ABC, abstractmethod

class CustomerInterface(ABC):

    @abstractmethod
    def create_user(self, name: str, last_name: str, gender: int, birthdate: str, phone:int, address:int):
        pass

    @abstractmethod
    def get_customer_by_id(self, id:int):
        pass

    @abstractmethod
    def delete_customer(self, customer_id:int):
        pass
