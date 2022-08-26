from abc import ABC, abstractmethod
from typing import List, Dict, Any
import datetime
from dataclasses import dataclass


@dataclass
class Order:
    symbol: str
    buy_sell: str
    size: int
    price: float


class Exchange(ABC):
    """
    Represents a connection to an exchange where
    the code can send orders to.
    """
    @abstractmethod
    def connect(self) -> None:
        """
        Establish connection to exchange.
        """
        pass

    @abstractmethod
    def get_quote(self, symbol: str) -> float:
        """
        Gets quote for symbol.
        """
        pass

    @abstractmethod
    def send_order(self, order: Order) -> int:
        """
        Sends order to exchange
        """
        pass


class NYSEExchange(Exchange):
    """
    Connect and send orders to NYSE exchange.
    """
    def connect(self) -> None:
        """
        Establish connection to exchange.
        """
        print("Connected to NYSE")

    def get_quote(self, symbol: str) -> float:
        """
        Gets quote for symbol.
        """
        return 130, 140

    def send_order(self, order: Order) -> int:
        """
        Sends order to exchange
        """
        print(f"{order} sent to NYSE @ {datetime.datetime.now()}")


class NASDAQExchange(Exchange):
    """
    Connect and send orders to NYSE exchange.
    """
    def connect(self) -> None:
        """
        Establish connection to exchange.
        """
        print("Connected to NASDAQ")

    def get_quote(self, symbol: str) -> float:
        """
        Gets quote for symbol.
        """
        return 135, 141

    def send_order(self, order: Order) -> int:
        """
        Sends order to exchange
        """
        print(f"{order} sent to NASDAQ @ {datetime.datetime.now()}")


class OrderRouter:
    """
    Sends buy or sell orders to an exchange.
    """
    def __init__(self, exchange: Exchange) -> None:
        self.exchange = exchange

    def send_order(self, order: Order) -> int:
        """
        Use exchange object to establish connection, then 
        send the order.
        """
        self.exchange.connect()
        if not self.check_spread(order):
            print(f"{order.price} is outside of spread!")
            return 0

        print(f"{order.price} is within spread!")
        self.exchange.send_order(order)
        print("Order sent.")

    def check_spread(self, order: Order) -> bool:
        """
        Check if price is within bid ask spread
        """
        bid, ask = self.exchange.get_quote(order.symbol)
        return bid <= order.price <= ask


def client():
    order = Order(
        symbol="META",
        buy_sell="S",
        size=345,
        price=135.0
    )
    nyse = NYSEExchange()
    router = OrderRouter(exchange=nyse)
    router.send_order(order=order)

client()