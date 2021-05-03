import random
import itertools
import collections

# Goals: start card, nibs/nobs, easier input for pre-determined hand, flushes, runs, pairs/multiples
# Big-time challenges: optimal peg counting factoring multiple players, percentage likelihood of pre-defined crib (may require complete overhaul)

class CribbageCalc:
    def calculate():
        def gen_hand():
            suits = ['C', 'S', 'H', 'D']
            values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            deck = [[v, s] for s in suits for v in values]
            hand = []
            quantity = 5
            hand_len = len(hand)

            while hand_len < quantity:
                card = deck[random.randint(0,51)]
                if card not in hand:
                    hand.append(card)
                    hand_len = len(hand)
            
            print(hand)
            count(hand)

        def count(hand):
            print('Calculating score...')
            score = 0
            hand_val = []
            n2 = 0
            for i in range(len(hand)):
                value = hand[n2][0]
                if value.upper() == 'J' or value.upper() == 'Q' or value.upper() == 'K':
                    hand_val.append(10)
                else:
                    hand_val.append(int(value))
                n2 += 1

            scorecard = [fifteens for i in range(len(hand_val) + 1) for fifteens in itertools.combinations(hand_val, i) if sum(fifteens) == 15]
            print(f'Fifteens identified: {scorecard}')

            for i in range(len(scorecard)):
                print('Fifteen, +2')
                score += 2

            suits = [suit for card in hand for suit in card[1]]
            for suit in suits:
                s_quant = suits.count(suits[0])
                if s_quant > 3:
                    score += s_quant
                    print(f'Flush, +{s_quant}')
                    break
                else:
                    pass

            print(f'Your hand is worth {score} points.')

        print('Enter your hand as follows:')
        verify2 = input('ex. King of Clubs, Ace of Clubs as: K C, 1 C or R for random: ')

        if verify2.upper() == 'R':
            gen_hand()
        else:
            n1 = 0
            pd_card = verify2.split(', ')
            pd_hand = []
            for i in range(5):
                pd_hand.append(pd_card[n1].split(' '))
                n1 += 1
            count(pd_hand)
    
CribbageCalc.calculate()