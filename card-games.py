import random
import sys


class Card(object):
	def __init__(self, value = "A", suit = "S"):
		super(Card, self).__init__()
		self.value = str(value)
		self.suit = { "S": u"\u2660", "C": u"\u2663", "H": u"\u2665", "D": u"\u2666" }[suit].encode("utf8")

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
		cardlists = [[] for _ in range(n)] # [[]]*n makes references, not full copies
		for i in range(len(self.cards)):
				cardlists[i%n].append(self.cards[i])
		return [Deck(cl) for cl in cardlists]


class Player(object):
	def __init__(self, deck = None):
		super(Player, self).__init__()
		self.deck = deck if deck else Deck()
		self.deck.shuffle()
		

def war(num_players = 4):
	deck = Deck().shuffle()
	decks = deck.split(num_players)
	human = Player(deck = decks[0])
	cpus = [Player(deck = decks[i+1]) for i in range(num_players-1)]
	# play game here, player.deck.cards.pop(0) removes and returns first card in player's deck
	return


def trash():
	return


if __name__ == "__main__":
	games = ["war", "trash"]

	if len(sys.argv) < 2:
		print("Available games:")
		for index, game in enumerate(games):
			print("  {0}: {1}".format(index, game.title()))
		try:
			choice = raw_input("Please enter a number or game title: ")
		except EOFError:
			choice = "0"
	else:
		choice = sys.argv[1]

	if choice.lower() in games:
		choice = choice.title()
	elif choice.isdigit() and int(choice) in range(len(games)):
		choice = games[int(choice)].title()
	else:
		raise ValueError("Choice must be a game number or title within the valid range 0-{0}.".format(len(games)-1))
	print("Choice: {0}".format(choice))

	exec(choice.lower()+"()")
