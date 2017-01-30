#Player's hands, up to 10
players = int(raw_input("Number of players"))
hands = [[(0, 'suit') for i in range(7)] for j in range(players)]
folded = [False for i in range(10)]

#Starting hand probability
pocket_pair = 3 / 51
suited_cards = 12 / 51

for flop in range(5):
    print 'FLOP ' + str(flop + 1)
    for hand in range(players):
        if (!folded[hand]):
            newCard = ( int(raw_input("Player " + str(hand + 1) + " val: ")), raw_input("Player " + str(hand + 1) + " suit: ") )
            hands[hand][flop + 2] = newCard
        