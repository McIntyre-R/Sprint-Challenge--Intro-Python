# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class




class Vehicle:
    pass

#Vehicle
class FlightVehicle(Vehicle):
    pass

#Vehicle => Flight Vehicle
class Airplane(FlightVehicle):
    pass


#Vehicle => Flight Vehicle
class Starship(FlightVehicle):
    pass


#Vehicle
class GroundVehicle(Vehicle):
    pass

#Vehicle => GroundVehicle
class Car(GroundVehicle):
    pass

#Vehicle => GroundVehicle
class Motorcycle(GroundVehicle):
    pass