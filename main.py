import random

def print_game():
    print("Players:")
    for p in players:
        print(p)
    print("Table:")
    print(table)

def discard_trios():
    pass

CARDS_PER_PLAYER = 7
NUMBER_OF_PLAYERS = 4

deck = [x for x in range(1,13)] * 3
random.shuffle(deck)

# Initialize players
players = [sorted(deck[i:i+8]) for i in range(0, NUMBER_OF_PLAYERS*CARDS_PER_PLAYER, CARDS_PER_PLAYER)]
visible_game = players.copy()
table = sorted(deck[CARDS_PER_PLAYER*NUMBER_OF_PLAYERS:])

print_game()

# Turn 0
## Remove standing trios

# Turn 1
ask_lowest()
