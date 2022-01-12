from abc import ABC, abstractmethod
import product


class Creator(ABC):
    @abstractmethod
    def _create_product(self) -> product.Product:
        pass

    def some_operation(self) -> str:
        concrete_product = self._create_product()
        return f"Creator: Performed some_operation with {concrete_product.operation()}"


class ConcreteCreatorOne(Creator):
    def _create_product(self) -> product.Product:
        return product.ProductA()


class ConcreteCreatorTwo(Creator):
    def _create_product(self) -> product.Product:
        return product.ProductB()