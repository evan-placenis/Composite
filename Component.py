from abc import ABC, abstractmethod
from Watt import Watt
from Currency import Currency

class Equiptment(ABC):

    def Name(self) -> str:
        return self.name
    @abstractmethod
    def Power() -> Watt:
        pass
    @abstractmethod
    def NetPrice() -> Currency():
        pass
    @abstractmethod
    def DiscountPrice() -> Currency():
        pass
    @abstractmethod
    def Add(e):
        pass
    @abstractmethod
    def Remove(e):
        pass
    @abstractmethod
    def CreateItorator():
        pass

# class FloppyDisk(Equiptment):
#     def __init__(self):
#         pass
    
#     def Power() -> Watt:
#         return Watt(10)

#     def NetPrice() -> Currency():
#         price = 50
#         return Currency(price)

#     def DiscountPrice() -> Currency():
#         discountPrice = 40
#         return Currency(discountPrice)

