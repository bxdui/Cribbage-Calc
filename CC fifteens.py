import random
import math
import itertools
from collections import deque

class CribbageCalc:
    def calculate():
        suits = ['C', 'S', 'H', 'D']
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [[v, s] for s in suits for v in values]
        quantity = 5
        loop_count = math.factorial(quantity)
        hand = []
        hand_val = []
        hand_len = len(hand)
        
        while hand_len < quantity:
            card = deck[random.randint(0,51)]
            if card not in hand:
                hand.append(card)
                hand_len = len(hand)
                hand_val.append(card[0])

        print(hand)

        verify = input("Count 15s? Y or N ")
        if verify == 'Y' or verify == 'y':
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

            calculate = [fifteens for i in range(len(hand_val)) for fifteens in itertools.combinations(hand_val, i) if sum(fifteens) == 15]
            
            for i in range(len(calculate)):
                score += 2
        else:
            print('Done') 

        print(score)   

    # def count(hand, loop_count):
        # count = deque([])
        # combo_set = []
        # n1 = 0
        # n2 = 0
        # score = 0

        # for i in range(loop_count):
        #     n1 = 0
        #     while sum(count) < 15:
        #         print('<15')
        #         card = hand[n1]
        #         value = card[0]
        #         if value == 'J' or value == 'Q' or value == 'K':
        #             count.append(10)
        #         else:
        #             count.append(int(value))
        #         print(count)
        #         n1 += 1
        #     n2 += 1

        #     if sum(count) == 15:
        #         print('=15')
        #         combo = [x for x in count]
        #         if combo not in combo_set:
        #             combo_set.append(combo)
        #             count.clear()
        #             score += 2
            
        #     if sum(count) > 15:
        #         print('>15')
        #         count.clear()
        # print(score)

CribbageCalc.calculate()