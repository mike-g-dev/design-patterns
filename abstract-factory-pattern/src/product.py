from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function(self) -> str:
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def useful_function(self) -> str:
        pass

    @abstractmethod
    def another_useful_function(self) -> str:
        pass


class ProductAOne(AbstractProductA):
    def useful_function(self) -> str:
        return f"Used useful_function on {self.__class__.__name__}"


class ProductATwo(AbstractProductA):
    def useful_function(self) -> str:
        return f"Used useful_function on {self.__class__.__name__}".upper()


class ProductBOne(AbstractProductB):
    def useful_function(self) -> str:
        return f"Used useful_function on {self.__class__.__name__}"

    def another_useful_function(self) -> str:
        return f"Used another_useful_function on {self.__class__.__name__}"


class ProductBTwo(AbstractProductB):
    def useful_function(self) -> str:
        return f"Used useful_function on {self.__class__.__name__}"

    def another_useful_function(self) -> str:
        result = self.useful_function()
        return f"Used another_useful_function on {self.__class__.__name__} with help from {result}"
