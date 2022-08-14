from abc import ABC, abstractmethod
from typing import List
import pandas as pd


class TradingStrategy(ABC):
    """
    Provides the interface for trading strategies to
    determine buy or sell actions based upon past market data,
    the current price of the instrument, and the methodology defined
    in subclasses who implement shouldBuy() and shouldSell() methods. 
    """
    @abstractmethod
    def shouldBuy(self) -> bool:
        """
        Defines methodology that determines if 
        the trader should buy the instrument.
        """
        pass

    @abstractmethod
    def shouldSell(self) -> bool:
        """
        Defines methodology that determines if 
        the trader should sell the instrument.
        """
        pass


class RollingAvgStrategy(TradingStrategy):
    """
    Rolling average trading strategy compares the present price to the 
    rolling average price. 
    If the rolling average price is below the present price, sell; if the
    rolling average price is above the present price, buy.
    """
    def __init__(self, 
        current_price: float,
        comparison_prices: List[float],
        window: int
    ) -> None:
        self.current_price = current_price
        self.comparison_prices = pd.Series(comparison_prices)
        self.window = window

    def shouldBuy(self) -> bool:
        rolling_avg = self.comparison_prices.rolling(self.window).mean()
        comparison_price = rolling_avg.values[-1]
        if not comparison_price:
            raise ValueError(f"Last price was NaN!")

        return comparison_price >= self.current_price

    def shouldSell(self) -> bool:
        rolling_avg = self.comparison_prices.rolling(self.window).mean()
        comparison_price = rolling_avg.values[-1]
        if not comparison_price:
            raise ValueError(f"Last price was NaN!")

        return comparison_price <= self.current_price


class Trader:
    """
    Subject who can execute a trading strategy
    """
    def __init__(self, strategy: TradingStrategy) -> None:
        self.strategy = strategy

    def executeStrategy(self) -> str:
        """
        Method called to execute a trading strategy.
        """
        if self.strategy.shouldBuy():
            return "BUY"
        if self.strategy.shouldSell():
            return "SELL"

def main():
    """
    Main client function passes a TradingStrategy type to Trader 
    who uses TradingStrategy.shouldBuy() and TradingStrategy.shouldSell()
    to make a trade.
    """
    prices = [12.0, 13.0, 15.0, 11.0, 10.0]

    strategy = RollingAvgStrategy(
        current_price=11.0,
        comparison_prices=prices,
        window=1
        )

    trader = Trader(strategy=strategy)

    print(f"{trader.executeStrategy()}")


if __name__ == "__main__":
    main()