from Composite import Chassis, Cabinit, Bus
from Composite import CompositeEquiptment
 

cabinit = Cabinit("PC Cabinit")
print("Created", cabinit.Name())

chassis = Chassis("PC Chassis")
print("Created", chassis.Name())

print(cabinit.Name(), "has power of", cabinit.NetPower().watt)


cabinit.Add(chassis)
print("Added " + chassis.Name() + " To " + cabinit.Name())


print("Total power of the cabinit now is: ",  cabinit.NetPower().watt)

bus = Bus("PC Bus")
print("Created", bus.Name())

cabinit.Add(bus)
print("Added " + bus.Name() + " To " + cabinit.Name())

print("Total power of the cabinit now is: ",  cabinit.NetPower().watt)

print("Total cost of cabinit is: ", cabinit.NetPrice().price)


