import random
import math
import itertools
from collections import deque

class CribbageCalc:
    def calculate():
        suits = ['C', 'S', 'H', 'D']
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [[v, s] for s in suits for v in values]
        quantity = 4
        hand = []
        hand_len = len(hand)
        
        while hand_len < quantity:
            card = deck[random.randint(0,51)]
            if card not in hand:
                hand.append(card)
                hand_len = len(hand)
                hand_val.append(card[0])

        verify = input("Count hand? Y or N: ")
        if verify == 'Y' or verify == 'y':
            CribbageCalc.count(hand, suits)

        print(hand)

    def count(hand, suits):
        score = 0
        hand_val = []
        n = 0
        for i in range(len(hand)):
            value = hand[n][0]
            if value == 'J' or value == 'Q' or value == 'K':
                hand_val.append(10)
            else:
                hand_val.append(int(value))
            n += 1

        scorecard = [fifteens for i in range(len(hand_val)) for fifteens in itertools.combinations(hand_val, i) if sum(fifteens) == 15]

        hand_suits = [suit for card in hand for suit in card[1]]

        n = -1

        for i in range(quantity):
            n += 1
            s_quant = hand_suits.count(hand_suits[n])
            if s_quant >= 4:
                score += 4

        for i in range(len(scorecard)):
            score += 2
    else:
        print('Done') 

    print(score)   

CribbageCalc.calculate()