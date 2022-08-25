from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    """
    Provides the interface to a service that 
    both the real service and proxy can implement.
    """
    @abstractmethod
    def operation(self) -> None:
        """
        Some operation.
        """
        pass


class RealService(ServiceInterface):
    """
    A service which provides some useful business logic.
    """
    def operation(self) -> None:
        print("Performing real service operation!")


class ProxyService(ServiceInterface):
    """
    A proxy for executing the real business logic encapsulated by
    the RealService.
    """
    def __init__(self, service: ServiceInterface) -> None:
        self.service = service

    def operation(self) -> None:
        """
        The operation can be wrapped in any logic but must contain
        the same interface as well as calling arguments as 
        the RealService.
        """
        print("Calling service from proxy!")
        return self.service.operation()


def client(service: ServiceInterface) -> None:
    """
    An example of some client code which 
    expects a ServiceInterface type -- not necissarily
    a ProxyService or RealService and performs an operation.
    """
    service.operation()

def main():
    service = RealService()
    client(service)

    proxy = ProxyService(service)
    client(proxy)

if __name__ == "__main__":
    main()