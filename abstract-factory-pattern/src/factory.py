"""
This module is responsible for declaring the factory interface for
instantiating products a and b. Crucially, the creation methods
on the factories return AbstractProduct subclasses; meaning, changes to
the concrete product methods do not affect the procedural logic involved with
creating and using them. Additionally, more proucts can be created as well as
more sophisticated factories to create and use them in custom use cases.
"""
from abc import ABC, abstractmethod
import product


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> product.AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> product.AbstractProductB:
        pass


class FactoryOne(AbstractFactory):
    def create_product_a(self) -> product.AbstractProductA:
        return product.ProductAOne()

    def create_product_b(self) -> product.AbstractProductB:
        return product.ProductBOne()


class FactoryTwo(AbstractFactory):
    def create_product_a(self) -> product.AbstractProductA:
        return product.ProductATwo()

    def create_product_b(self) -> product.AbstractProductB:
        return product.ProductBTwo()
