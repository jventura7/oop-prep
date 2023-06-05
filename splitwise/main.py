# Classes:
# User:
#   - userId, name, email, mobile number
# Expense:
#   - Could be either Equal, Exact, Percent
# Show: 
# Splitwise:
#   - has users, types of expenses, 
# --
# users = {user1: {}, user2: {}, etc...}
#
# flow:
# create users -> init splitwise -> add users -> SHOW all user balances
#                                             -> create an EXPENSE
from abc import ABC, abstractmethod

"User Class"
class User:
  def __init__(self, id, name, email, number):
    self._id = id
    self._name = name
    self._email = email
    self._number = number

  def get_id(self):
    return self._id
  
  def get_name(self):
    return self._name

  def get_email(self):
    return self._email
  
  def get_number(self):
    return self._number

"Expenses Class"
class Expense(ABC):
  def __init__(self, user_db):
    self._user_db = user_db

  def _update_db(self, user_paying, user_who_owes, amount):
    self._user_db.update(user_paying, user_who_owes, amount)

  @abstractmethod
  def split(self, user_paying, users_to_split, amounts):
    pass

class Equal(Expense):
  def __init__(self, user_db):
    super().__init__(user_db)

  def split(self, user_paying, users_to_split, amount):
    pass

class Exact(Expense):
  def __init__(self, user_db):
    super().__init__(user_db)

  def split(self, user_paying, users_to_split, exact_amounts):
    pass

class Percent(Expense):
  def __init__(self, user_db):
    super().__init__(user_db)

  def split(self, user_paying, users_to_split, percentages):
    pass

"Show Class"
class Show:
  @staticmethod
  def show_balances(users_db):
    users_database = users_db.get_users_db()

    if all(value == {} for value in users_database.values()):
      print('No balances')
    
    for user_id in users_database:
      user = users_db.get_user_from_id(user_id)

      if users_database[user_id]:
        print(f'{user.get_name()} is owed:\n')
        
        for user_owing_id in users_database[user_id]:
          user_owing = users_db.get_user_from_id(user_owing_id)
          print(f'{users_database[user_id][user_owing_id]} from {user_owing.get_name()}\n')

"UserDB Class"
class UserDB:
  def __init__(self):
    self._users_db = {}
    self._id_to_user = {}

  def get_users_db(self):
    return self._users_db
  
  def add_user(self, user):
    self._users_db[user.get_id()] = {}
    self._id_to_user[user.get_id()] = user
  
  def remove_user(self, user):
    del self._users_db[user.get_id()]
    del self._id_to_user[user.get_id()]

  def get_user_from_id(self, user_id):
    return self._id_to_user[user_id]

  def update_owing_this_user(self, user_paying_id, user_who_owes_id, amount):
    if user_paying_id not in self._users_db:
      raise ValueError('Not a valid id')

    self._users_db[user_paying_id][user_who_owes_id()] += \
      self._users_db.get(0, self._users_db[user_paying_id][user_who_owes_id]) + amount
  
"Splitwise Class"
class Splitwise:
  def __init__(self, users_db):
    self._users_db = users_db

  def driver(self):
    while True:
      action = input()
      action = action.split(' ')
      print(action)
      if action[0] == 'SHOW':
        Show.show_balances(self._users_db)
      if action[0] == 'EXPENSE':
        pass

  def _expense(self, type):
    pass


"Testing"
# init users and db
users = [User(1, 'John', 'john@gmail.com', 5714328488), User(2, 'Keith', 'keith@gmail.com', 5713211033), \
         User(3, 'Marco', 'marco@gmail.com', 2330959593), User(4, 'Polo', 'polo@gmail.com', 4329594022)]
users_db = UserDB()

# add to db
for user in users:
  users_db.add_user(user)

# init program
splitwise = Splitwise(users_db)
splitwise.driver()