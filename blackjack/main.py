# - 2 players, including dealer
# - one deck of cards, which is refilled and reshuffled after each round
# - the player will start with an amount of money and can place a bet before each round
# - the game will go until the player has lost all their money or decide to stop

# Classes:
# Player - 
#   can either be gambler or dealer
# Gambler 
#   store their money 
#   place a bet
#
# Deck:
#   init 52 cards 
#   shuffle method
#   draw card method
# 
# Card:
#   1 card
#   specify suit and value
# 
# Hand: 
#   holds cards in an array 
#   keeps track of score
#   add card method
#   determines if there hand busted

from enum import Enum
from abc import ABC, abstractmethod
from random import randint

class Suit(Enum):
  CLUBS = 'clubs',
  HEARTS = 'diamonds',
  SPADES = 'spades',
  DIAMONDS = 'diamonds'

class Card:
  def __init__(self, suit, value):
    self.__suit = suit
    self.__value = value
  
  def getSuit(self):
    return self.__suit

  def getValue(self):
    return self.__value

class Deck:
  def __init__(self):
    self.__cards = self.__initCards()
    self.shuffle()

  def __initCards(self):
    cards = []
    for suit in Suit:
      for value in range(1, 14):
        cards.append(Card(suit, min(value, 10)))
    return cards
  
  def draw(self):
    return self.__cards.pop()

  def shuffle(self):
    for i in range(len(self.__cards)):
      r = randint(0, 51)
      self.__cards[i], self.__cards[r] = self.__cards[r], self.__cards[i]






class Hand:
  def __init__(self):
    self.__cards = []
    self.__score = 0
  
  def addCard(self, card):
    value = card.getValue()
    if self.__score + value > 21: 
      return False
    
    self.__score += value
    self.__cards.append(card)
    return True
  
  def getScore(self):
    return self.__score

  def getCards(self):
    return self.__cards
  






class Player(ABC):
  def __init__(self, hand):
    self.__hand = hand
  
  def getHand(self):
    return self.__hand
  
  # player and dealer have different ways to make move. The UI will ask the player if they wish to make a move, 
  # while the dealer has to make a move until they reach players points or bust
  @abstractmethod
  def makeMove(self):
    pass

class Gambler(Player):
  def __init__(self, money, hand):
    self.__money = money
    super().__init__(hand)

  def getMoney(self):
    return self.__money
  
  def setMoney(self, money):
    self.__money += money
  
  def makeMove(self, card):
    self.__hand.addCard(card)
    return self.__hand.getScore() > 21

class Dealer(Player):
  def __init__(self, hand):
    super().__init__(hand)

  def makeMove(self):
    pass
  






class BlackjackGame:
  def __init__(self):
    self.__gambler = Gambler(0, Hand())
    self.__dealer = Dealer(Hand())
    self.__deck = Deck()

  def playRound(self, bet):
    self.dealCards()
    self.showInitialCards()
    if not self.userTurn(bet): return 
    self.determineWinner(bet)

  # draw two cards for the dealer and two cards for player
  def dealCards(self):
    for i in range(4):
      card = self.__deck.draw()
      if i % 2 == 0: self.__gambler.getHand().addCard(card)
      else: self.__dealer.getHand().addCard(card)

  # show the gambler the dealer's card
  def showInitialCards(self):
    dealerCard1, _ = self.__dealer.getHand().getCards()
    gamblerCard1, gamblerCard2 = self.__gambler.getHand().getCards()
    print(dealerCard1.getValue(), dealerCard1.getSuit())
    print(f'Dealer cards: *flipped* {dealerCard1.getValue()} of {dealerCard1.getSuit()}')
    print(f'Your cards: {gamblerCard1.getValue()} of {gamblerCard1.getSuit()} and {gamblerCard2.getValue()} of {gamblerCard2.getSuit()} ')


  def userTurn(self, bet):
    draw = input(f'Would you like to draw? (Y/N)\n')
    while draw == 'Y':
      cardDrawed = self.__deck.draw()
      if not self.__gambler.makeMove(cardDrawed):
        print('You busted!\n')
        self.__gambler.setMoney(self.__gambler.getMoney() - bet)
        return False
      else:
        print(f'Your total score is: {self.__gambler.getHand().getScore()}\n')
        draw = input('Would you like to draw? (Y/N)\n')
    
    print(f'Your final score is {self.__gambler.getHand().getScore()}')
    return True
  
  def determineWinner(self, bet):
    net = 0
    if self.__gambler.getHand().getScore() > self.__dealer.getHand().getScore():
      net = bet
      print(f'You won {bet}!')
    else:
      net = -bet
      print(f'You lost {bet}...')
    self.__gambler.setMoney(self.__gambler.getMoney() + net)

  def playGame(self):
    self.buyPlayerIn()
    play = 'Y'
    while play == 'Y':
      bet = input(f'How much would you like to bet?\n')
      self.playRound(int(bet))
      if self.__gambler.getMoney() <= 0:
        print('You lost all your money!')
        return
      play = input(f'Would you like to play another round? (Y/N)\n')
    print(f'Money left: {self.__gambler.getMoney()}')


  def buyPlayerIn(self):
    buyIn = int(input('How much would you like to buy in for?\n'))
    self.__gambler.setMoney(buyIn)
  

game = BlackjackGame()
game.playGame()