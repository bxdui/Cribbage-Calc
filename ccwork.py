import random
import itertools

# Goals: start card, nibs/nobs, easier input for pre-determined hand, flushes, runs, pairs/multiples
# Convert hand to dictionary format, including full text for suits and face names. Use full text to denote suits and values

# Long-term challenges: optimal peg counting factoring multiple players, percentage likelihood of pre-defined crib (may require complete overhaul)

class CribbageCalc:
    def calculate():
        def gen_hand():
            suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
            values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
            deck = [[v, s] for s in suits for v in values]
            hand = []
            hand_len = len(hand)

            while hand_len < 5:
                card = deck[random.randint(0,51)]
                if card not in hand:
                    hand.append(card)
                    hand_len = len(hand)
            
            print(f'Your hand: {hand}')
            count(hand)

        def count(hand):
            # Convert face cards to 10
            print('Calculating score...')
            score = 0
            hand_val = []
            for value in hand:
                try:
                    int(value[0]) == True
                except:
                    hand_val.append(10)
                else:
                    hand_val.append(int(value[0]))

            # Find fifteens
            scorecard = [fifteens for i in range(len(hand_val) + 1) for fifteens in itertools.combinations(hand_val, i) if sum(fifteens) == 15]
            scorecard_len = len(scorecard)
            print(f'Combos: {scorecard}')
            print(f'{scorecard_len} fifteen(s), +{scorecard_len * 2}')
            for i in range(len(scorecard)):
                score += 2

            # ID suits and check for flush
            suits = [suit for card in hand for suit in card[1]]
            for suit in suits:
                s_quant = suits.count(suits[0])
                if s_quant > 3:
                    score += s_quant
                    print(f'Flush, +{s_quant}')
                    break
                else:
                    pass
                
            # Print score
            print(f'Your hand is worth {score} points.')

        # ID hand to count
        print('Enter your hand as follows:')
        verify2 = input('ex. King of Clubs, Ace of Clubs as: "K Clubs, 1 Clubs" or "R" for random: ')

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