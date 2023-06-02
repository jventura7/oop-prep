# Requirements:
# 1. build out pieces that have unique moves (pawn, king, queen, rook, knight)
# 2. have 2 players that can play the game (take turns making moves, has pieces, can capture pieces, ..)
# 3. build out a board (grid)
# 4. build out chess game (made up of players, pieces, board)
# 
# Classes:
# Piece(ABC):
#   - has a position
#   - has a way to make a move
#     - if a piece makes a move and lands on oppponents piece, then capture
# Pawn:
# King:
# Queen:
# Rook:
# Knight:
# 
# Player:
#   - pieces = {} of all pieces as key and position as value
#   - makeMove function

from abc import ABC, abstractmethod
from enum import Enum

class PieceColor(Enum):
  WHITE = 0,
  BLACK = 1

"PIECE CLASSES"
class Piece(ABC):
  def __init__(self, x, y, color):
    self.__position = [x, y]
    self.__color = color
  
  def get_position(self):
    return self.__position
  
  def set_position(self, x, y):
    self.__position = [x, y]

  def get_color(self):
    return self.__color

  @abstractmethod
  def move(self, dx, dy):
    pass

class Pawn(Piece):
  def __init__(self, x, y, color):
    super().__init__(x, y, color)
  
  def move(self, dx, dy):
    pass

class King(Piece):
  def __init__(self, x, y, color):
    super().__init__(x, y, color)
  
  def move(self, dx, dy):
    pass

class Queen(Piece):
  def __init__(self, x, y, color):
    super().__init__(x, y, color)
  
  def move(self, dx, dy):
    pass

class Rook(Piece):
  def __init__(self, x, y, color):
    super().__init__(x, y, color)
  
  def move(self, dx, dy):
    x, y = self.get_position()
    if dx != x and dy != y:
      raise ValueError('Invalid move for a rook, please move in a straight line')
    self.set_position(dx, dy)

class Bishop(Piece):
  def __init__(self, x, y, color):
    super().__init__(x, y, color)

  def move(self, dx, dy):
    pass

class Knight(Piece):
  def __init__(self, x, y, color):
    super().__init__(x, y, color)
  
  def move(self, dx, dy):
    pass
"PIECE CLASSES"











"PIECES CLASS"
class Pieces:
  def __init__(self):
    self.__pieces = set()

  def get_pieces(self):
    return self.__pieces

  def add_piece(self, piece):
    self.__pieces.add(piece)

  @abstractmethod
  def init_pieces(self):
    pass

  @abstractmethod
  def init_pawns(self):
    pass

  @abstractmethod
  def init_rooks(self):
    pass
  
  @abstractmethod
  def init_knights(self):
    pass

  @abstractmethod
  def init_bishops(self):
    pass

  @abstractmethod
  def init_queen(self):
    pass
  
  @abstractmethod
  def init_king(self):
    pass

class BlackPieces(Pieces):
  def __init__(self):
    super().__init__()
    self.init_pieces()

  def init_pieces(self):
    self.init_pawns()
    self.init_bishops()
    self.init_rooks()
    self.init_knights()
    self.init_king()
    self.init_queen()

  def init_pawns(self):
    row = 1
    for i in range(8):
      self.add_piece(Pawn(row, i, PieceColor.BLACK))
  
  def init_rooks(self):
    row = 0
    self.add_piece(Rook(row, 0, PieceColor.BLACK))
    self.add_piece(Rook(row, 7, PieceColor.BLACK))
  
  def init_knights(self):
    row = 0
    self.add_piece(Knight(row, 1, PieceColor.BLACK))
    self.add_piece(Knight(row, 6, PieceColor.BLACK))

  def init_bishops(self):
    row = 0
    self.add_piece(Bishop(row, 2, PieceColor.BLACK))
    self.add_piece(Bishop(row, 5, PieceColor.BLACK))

  def init_queen(self):
    row = 0
    self.add_piece(Queen(row, 3, PieceColor.BLACK))
  
  def init_king(self):
    row = 0
    self.add_piece(King(row, 4, PieceColor.BLACK))

class WhitePieces(Pieces):
  def __init__(self):
    super().__init__()
    self.init_pieces()

  def init_pieces(self):
    self.init_pawns()
    self.init_bishops()
    self.init_rooks()
    self.init_knights()
    self.init_king()
    self.init_queen()

  def init_pawns(self):
    row = 6
    for i in range(8):
      self.add_piece(Pawn(row, i, PieceColor.WHITE))
  
  def init_rooks(self):
    row = 7
    self.add_piece(Rook(row, 0, PieceColor.WHITE))
    self.add_piece(Rook(row, 7, PieceColor.WHITE))
  
  def init_knights(self):
    row = 7
    self.add_piece(Knight(row, 1, PieceColor.WHITE))
    self.add_piece(Knight(row, 6, PieceColor.WHITE))

  def init_bishops(self):
    row = 7
    self.add_piece(Bishop(row, 2, PieceColor.WHITE))
    self.add_piece(Bishop(row, 5, PieceColor.WHITE))

  def init_queen(self):
    row = 7
    self.add_piece(Queen(row, 3, PieceColor.WHITE))
  
  def init_king(self):
    row = 7
    self.add_piece(King(row, 4, PieceColor.WHITE))
"PIECES CLASS"









"PLAYER CLASS"
class Player(ABC):
  def __init__(self, pieces):
    self.__pieces = pieces
    self.__captured = set()

  def get_pieces(self):
    return self.__pieces.get_pieces()

  def get_captured(self):
    return self.__captured

  def capture(self, piece):
    return self.__captured.append(piece)
"PLAYER CLASS"



# playerWhite = set(Pawn, Pawn, Pawn, Pawn, Queen, King, ...)
initBlackPieces = BlackPieces()
initWhitePieces = WhitePieces()
playerBlack = Player(initBlackPieces)
playerWhite = Player(initWhitePieces)
print(playerBlack.get_pieces())
