from abc import ABC, abstractmethod
class Equiptment(ABC):
    def __init__(self):
        self.name: str = "test"

    def Name(self) -> str:
        return self.name
    @abstractmethod
    def Power() :
        pass
    @abstractmethod
    def NetPrice():
        pass
    @abstractmethod
    def DiscountPrice():
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