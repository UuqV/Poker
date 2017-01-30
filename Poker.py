import math

#Player's hands, up to 10
players = int(raw_input("Number of players"))

#The value (0, 'suit') means a card is unknown to the program
hands = [[(0, 'suit') for i in range(7)] for j in range(players)]
status = ['None' for i in range(10)]

#Starting hand probability
pocket_pair = 3 / 51
suited_cards = 12 / 51

#Combinations
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

#Reads the domination potential of a hand
def eval_hand():
    for card_one in hands[0]:
        if card_one[1] != 'suit':
            for card_two in hands[0]:
                if card_two[1] != 'suit':
                    if card_one[0] == card_two[0]:
                        status[0] = 'Pair'
                        return
    status[0] = 'None'

#The base probability that a flop trumps an already held pocket pair
def pocket_pair_flop_recalc(rank):
    return float(nCr(((4 * rank) - 6), 3)) / nCr(50, 3)

#Beginning deal
for initCard in range(2):
    newCard = ( int(raw_input('User card ' + str(initCard + 1) + ' val: ')), raw_input('User card ' + str(initCard + 1) + ' suit: ') )
    hands[0][initCard] = newCard
    
eval_hand();
if status[0] == 'Pair':
    print hands[0][0][0]
    print pocket_pair_flop_recalc(hands[0][0][0])


for flop in range(5):
    print 'FLOP ' + str(flop + 1)
    for hand in range(players):
        if status[hand] != 'Folded':
            newCard = ( int(raw_input("Player " + str(hand + 1) + " val: ")), raw_input("Player " + str(hand + 1) + " suit: ") )
            hands[hand][flop + 2] = newCard
    