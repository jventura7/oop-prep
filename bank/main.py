# Entities:
#   Customer:
#     - can open a savings or checking account (dont have to)
#     - if they have an account, they can deposit or withdraw money
#     - they can take out loans
#     - they can apply for credit cards
#   Teller:
#   Account:
#     - Savings 
#     - Checking
#   Card:
#     - Credit Card
#     - Debit Card ?
#   Loan:
#     - ...
#   Bank: 
#     - Branch
#     - Headquarters
#
# flow:
# create a customer -> customer goes to bank and asks to open a savings account -> bank finds a free bank teller who 
# can perform this for the customer -> teller performs the transaction -> customer now has a savings account

from abc import ABC, abstractmethod

class Card(ABC):
   @abstractmethod
   def pay(self, amount):
      pass


class CreditCard:
    def __init__(self, monthly_limit):
      self._monthly_limit = monthly_limit
    
    def pay(self, amount):
       pass

    def pay_off(self):
       pass

class DebitCard:
  def __init__(self):
      self._balance = 0

  def pay(self, amount):
    pass

  def add_money(self, amount):
     pass
