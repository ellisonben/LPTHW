deck = []

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
names = [["Two", 2], ["Three", 3], ["Four", 4], ["Five", 5],
        ["Six", 6], ["Seven", 7], ["Eight", 8], ["Nine", 9],
        ["Ten", 10], ["Jack", 10], ["Queen", 10], ["King", 10], ["Ace", 11]]

for i in range(6):
    for suit in suits:
        for name in names:
            deck.append([suit, name])

def pop_deck():
    print deck.pop()

print len(deck)

pop_deck()

print len(deck)
      

