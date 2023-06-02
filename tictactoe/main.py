# Marker - either X or O (can be made extensible to be another character)
# Player - game will have 2 players each with their own unique marker, can also place marker
# Board - the board will init empty and will have cells where player can place marker
# Game - the game will contain a board and the players and will begin the game loop
#      - game will also keep track of the rules (validation)

from enum import Enum

class MarkerType(Enum):
  EMPTY = '-'
  X = 'X'
  O = 'O'

"Player Class"
class Player:
  def __init__(self, name, marker):
    self._name = name
    self._marker = marker
  
  def get_name(self):
    return self._name
  
  def get_marker(self):
    return self._marker

"Board Class"
class Board:
  def __init__(self, size):
    self._board = self._initBoard(size)
    self._size = size
  
  def _initBoard(self, size):
    return [[MarkerType.EMPTY for _ in range(size)] for _ in range(size)]

  def _in_range(self, row, col):
    return row >= 0 and row < self._size and col >= 0 and col < self._size

  def get_size(self):
    return self._size

  def get_marker_at(self, row, col):
    return self._board[row][col]

  def place_marker(self, row, col, marker):
    if not self._in_range(row, col):
      raise ValueError('Error: position out of bounds!')
    if self._board[row][col] != MarkerType.EMPTY:
      raise ValueError('Error: Position already taken!')
    self._board[row][col] = marker
  
  def print_board(self):
    print('Board:')
    for i in range(self._size):
      row = []
      for j in range(self._size):
        row.append(self._board[i][j].value)
        row.append(' ')
      print("".join(row))

"Game Class"
class Game:
  def __init__(self, board):
    self._board = board
    self._players = []

  def play_game(self):
    finished = False
    while not finished:
      finished = self._play_turn()

  def add_player(self, player):
    self._players.append(player)

  def _play_turn(self):
    for player in self._players:
      self._board.print_board()
      while True:
        try:
          row = int(input(f'{player.get_name()}, what row would you like to place your marker at? '))
          col = int(input(f'{player.get_name()}, what column would you like to place your marker at? '))
          self._board.place_marker(row, col, player.get_marker())
          if self._check_win(row, col, player.get_marker()): 
            self._board.print_board()
            print(f'{player.get_name()} has won!')
            return True
          break
        except Exception as e: 
          print(e)
    return False

  def _check_win(self, row, col, marker):
    return self._check_col(col, marker) or self._check_row(row, marker) or \
           self._check_anti_diagonal(marker) or self._check_diagonal(marker)

  def _check_diagonal(self, marker):
    for i in range(self._board.get_size()):
      if self._board.get_marker_at(i, i) != marker:
        return False
    return True

  def _check_anti_diagonal(self, marker):
    for i in range(self._board.get_size()):
      if self._board.get_marker_at(self._board.get_size() - i - 1, i) != marker:
        return False
    return True

  def _check_row(self, row, marker):
    for i in range(self._board.get_size()):
      if self._board.get_marker_at(row, i) != marker:
        return False
    return True

  def _check_col(self, col, marker):
    for i in range(self._board.get_size()):
      if self._board.get_marker_at(i, col) != marker:
        return False
    return True


"Testing"
size = int(input('Please input grid size: '))
board = Board(size)

player1Name = input('Player 1 Name: ')
player2Name = input('Player 2 Name: ')

player1 = Player(player1Name, MarkerType.X)
player2 = Player(player2Name, MarkerType.O)

game = Game(board)
game.add_player(player1)
game.add_player(player2)
game.play_game()
