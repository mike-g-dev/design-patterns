from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ProductA(Product):
    def operation(self) -> str:
        return "{Result of ProductA()}"


class ProductB(Product):
    def operation(self) -> str:
        return "{Result of ProductB()}"
