import random


suitdict = { "S": u"\u2660", "C": u"\u2663", "H": u"\u2665", "D": u"\u2666" }


class Card(object):
	def __init__(self, value = "A", suit = "S"):
		super(Card, self).__init__()
		self.value = str(value)
		self.suit = suitdict[suit].encode("utf8")

	def __str__(self):
		return str(self.value)+str(self.suit)


class Deck(object):
	def __init__(self, cards = None):
		super(Deck, self).__init__()
		self.cards = cards if cards else [Card(v, s) for v in range(2, 11)+["J", "Q", "K", "A"] for s in ["S", "C", "H", "D"]]

	def __str__(self):
		return ", ".join([str(c) for c in self.cards])

	def shuffle(self):
		random.shuffle(self.cards)
		return self

	def split(self, n = 2):
		cardlists = [[] for _ in range(n)] # since [[]]*n makes references, not full copies
		for i in range(len(self.cards)):
				cardlists[i%n].append(self.cards[i])
		return [Deck(cl) for cl in cardlists]


class Player(object):
	def __init__(self, deck = None):
		super(Player, self).__init__()
		self.deck = deck if deck else Deck()
		self.deck.shuffle()


if __name__ == "__main__":
	d = Deck()
	print(d)
	d.shuffle()
	print(d)
	for s in d.split(2):
		print(s)
