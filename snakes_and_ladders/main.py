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
from random import randint


"Dice Class"
class Dice:
  def __init__(self, size):
    self._sides = [i + 1 for i in range(size)]
  
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
  
  def get_snakes(self):
    return self._snakes

  def _init_snakes(self):
    return {10: 8, 32: 8, 43: 17, 64: 49, 88: 32}


"Ladders Class"
class Ladders:
  def __init__(self, size):
    self._ladders = self._init_ladders()
    self._size = size
  
  def get_ladders(self):
    return self._ladders
  
  def _init_ladders(self):
    return {3: 10, 8: 20, 40: 46, 24: 65, 84: 92}


"Board Class"
class Board:
  def __init__(self, size, snakes, ladders):
    self._board = [i + 1 for i in range(size)]
    self._snakes = snakes
    self._ladders = ladders
    self._size = size

  
  def get_value_at_position(self, position):
    # position is at snake head so move to tail
    if position in self._snakes.get_snakes():
      print('Landed at a snake head!')
      return self._snakes.get_snakes()[position]
    
    # if position is at ladder start move to ladder end
    if position in self._ladders.get_ladders():
      print('Landed at a ladder!')
      return self._ladders.get_ladders()[position]

    return 0

  def get_size(self):
    return self._size


"Game Class"
class Game:
  def __init__(self, die):
    self._die = die
    self._players = []

  def _add_player(self, player):
    self._players.append(player)

  def _init_players(self):
    num_players = int(input('How many players? '))
    for i in range(num_players):
      player_name = input(f'Player {i + 1} name: ')
      self._add_player(Player(player_name))

  def _init_board_and_pieces(self):
    board_size = int(input('How many tiles on the board? '))
    snakes = Snakes(board_size)
    ladders = Ladders(board_size)
    self._board = Board(board_size, snakes, ladders)

  def _play_round(self):
    for player in self._players:
      print(f"It's {player.get_name()}'s turn!\n")
      dice_roll = self._die.roll().value
      player_position = player.get_position()
      new_player_position = player_position + dice_roll
      print(f"{player.get_name()} rolled a {dice_roll}")
      while self._board.get_value_at_position(new_player_position) != 0:
        new_player_position = self._board.get_value_at_position(new_player_position)
      print(f"{player.get_name()} moved from {player_position} to {new_player_position}")
      player.update_position(new_player_position)
      if new_player_position == self._board.get_size(): 
        print(f"{player.get_name()} won!")
        return True
    return False

  def play_game(self):
    self._init_players()
    self._init_board_and_pieces()
    game_over = False
    while not game_over:
      game_over = self._play_round()


"Testing"
die = Dice(6)
game = Game(die)
game.play_game()
