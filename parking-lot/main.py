# Enumerations
from enum import Enum
from abc import ABC, abstractmethod

# Enumerations
class PaymentStatus(Enum):
    COMPLETED = 1
    FAILED = 2
    PENDING = 3
    UNPAID = 4
    REFUNDED = 5

class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5
  
# Custom data types
class Person:
    def __init__(self, name, address, phone, email):
        self._name = name
        self._address = address
        self._phone = phone
        self._email = email
    
class Address:
    def __init__(self, zip_code, address, city, state, country):
        self._zip_code = zip_code
        self._address = address
        self._city = city
        self._state = state
        self._country = country

# Parking Spot
class ParkingSpot(ABC):
    def __init__(self, id, isFree, vehicle):
        self._id = id
        self._isFree = isFree
        self._vehicle = vehicle
    
    def get_is_free(self):
        return self._isFree

    @abstractmethod
    def assign_vehicle(self):
        pass
    
    def remove_vehicle(self):
        pass
  
    
# Handicapped Parking Spot
class Handicapped(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self):
        pass
  
# Compact Parking Spot
class Compact(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self):
        pass
  
# Large Parking Spot
class Large(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
      super().__init__(id, isFree, vehicle)

    def assign_vehicle(self, vehicle):
      pass

# Motorcycle Parking Spot
class Motorcycle(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
      super().__init__(id, isFree, vehicle)

    def assign_vehicle(self, vehicle):
      pass

