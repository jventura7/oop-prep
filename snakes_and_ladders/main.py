# Snakes:
#   - has start and end
# Ladders:
#   - has start and end
# Player:
#   - has a name
#   - has initlal position (0)
#   - can move to new position
# Dice:
#   - has 6 sides
#   - can get random side (roll)
# Board:
#   - snakes and ladders (gamepiece) part of board (composition)
#   - can have player on position (aggregation)
#   - can place a game piece
# Game:
#   - has a board and players
#   - controls the flow of the game

from enum import Enum
from random import randint

"Dice Sides"
class Sides(Enum):
  ONE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6

"Dice Class"
class Dice:
  def __init__(self):
    self._sides = [side for side in Sides]
  
  def roll(self):
    return self._sides[randint(0, len(self._sides) - 1)]

"GamePiece Class"
class GamePiece:
  def __init__(self, start, end):
    self._start = start
    self._end = end
  
  def get_start(self):
    return self._start

  def get_end(self):
    return self._end


"Player Class"
class Player:
  def __init__(self, name):
    self._position = 0
    self._name = name
  
  def get_name(self):
    return self._name

  def get_position(self):
    return self._position
  
  def update_position(self, new_position):
    self._position = new_position

"Snakes Class"
class Snakes:
  def __init__(self, size):
    self._snakes = self._init_snakes()
    self._size = size
  
  def _init_snakes(self):
    pass


"Ladders Class"
class Ladders:
  def __init__(self, size):
    self._ladders = self._init_ladders()
    self._size = size
  
  def _init_ladders(self):
    pass


"Board Class"
class Board:
  def __init__(self, size, snakes, ladders):
    self._board = [i + 1 for i in range(size)]
    self._snakes = snakes
    self._ladders = ladders

  
  def get_value_at_position(self, position):
    # position is at snake head so move to tail
    if position in self._snakes:
      return self._snakes[position]
    
    # if position is at ladder start move to ladder end
    if position in self._ladders:
      return self._ladders[position]

    return 0
 

"Testing"
die = Dice()
print(die.roll())

