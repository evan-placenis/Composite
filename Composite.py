
from Equiptment import Equiptment
from Watt import Watt
from Currency import Currency

class CompositeEquiptment(Equiptment):
    equip = {}
    def __init__(self):
        pass

    def NetPower(self) -> Watt:
        totalPower = 0
        for key, value in self.equip.items():
            totalPower += value

        return Watt(totalPower)

    def NetPrice(self) -> Currency:
        totalPrice = 0
        for key, value in self.equip.items():
            totalPrice += key.Price().price
        
        return Currency(totalPrice)

    def DiscountPrice(self) -> Currency:
        discountPrice = 40
        return Currency(discountPrice)
    
    def Add(self, e:Equiptment):
        self.equip[e] = e.Power().watt
        
    
    def Remove(self, e:Equiptment):
        del self.equip[e]

    def CreateItorator(self):
        print("all equiptment in composite")
        for key, value in self.equip:
            print(key)

class Chassis (CompositeEquiptment):
    def __init__(self, name):
        self.name = name

    def Power(self) -> Watt:
        return Watt(20)

    def Price(self) -> Currency:
        price = 70
        return Currency(price)

    def DiscountPrice() -> Currency:
        discountPrice = 50
        return Currency(discountPrice)
    

class Cabinit (CompositeEquiptment):
    def __init__(self, name):
        self.name = name

    def Power(self) -> Watt:
        return Watt(0)

    def Price(self) -> Currency:
        price = 20
        return Currency(price)

    def DiscountPrice(self) -> Currency:
        discountPrice = 20
        return Currency(discountPrice)
    
class Bus (CompositeEquiptment):
    def __init__(self, name):
        self.name = name

    def Power(self) -> Watt:
        return Watt(30)

    def Price(self) -> Currency:
        price = 10
        return Currency(price)

    def DiscountPrice(self) -> Currency:
        discountPrice = 5
        return Currency(discountPrice)


