import sys
from cards import Deck, Player


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
