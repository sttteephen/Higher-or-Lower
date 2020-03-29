import random

class Card:

	def __init__(self, suit, number):
		if suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
			self._suit = suit
		else:
			print("That's not a valid suit.")

		if number in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
			self._number = number
		else:
			print("That is not a valid number.")

	def __repr__(self):
		return self._number + " of " + self._suit

	@property
	def suit(self):
		return self._suit

	@property
	def number(self):
		return self._number

	@number.setter
	def number(self, number):
		if number in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
			self._number = number
		else:
			print("That is not a valid number.")
	
	@suit.setter
	def suit(self, suit):
		if suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
			self._suit = suit
		else:
			print("That's not a valid suit.")



class Deck:

	def __init__(self):
		self._cards = []
		self.populate()

	def __repr__(self):
		deck_str = ''
		for card in self._cards:
			deck_str = (deck_str + str(card) + ', ')

		return deck_str[:(len(deck_str)-2)]

	def populate(self):
		number_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		suit_list = ['Clubs','Diamonds','Hearts','Spades']
		self._cards = [Card(s, n) for s in suit_list for n in number_list]

	def shuffle(self):
		random.shuffle(self._cards)