import random
import math
from collections import deque

class CribbageCalc:
    def novel_count():
        def generate_hand():
            suits = ['C', 'S', 'H', 'D']
            values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            deck = [[v, s] for s in suits for v in values]
            quantity = 5
            loop_count = math.factorial(quantity)
            hand = []
            hand_len = len(hand)
            
            while hand_len < quantity:
                card = deck[random.randint(0,51)]
                if card not in hand:
                    hand.append(card)
                    hand_len = len(hand)
            print(hand)

        def count(hand, loop_count):
            count = deque([])
            combo_set = {}
            n = 0
            score = 0

            for i in range(loop_count):
                while sum(count) < 15:
                    card = hand[n]
                    value = card[0]
                    if value == 'J' or value == 'Q' or value == 'K':
                        count.append(10)
                    else:
                        count.append(value)
                    n += 1

                if sum(count) == 15:
                    combo = [x for x in count]
                    if combo not in combo_set:
                        combo_set.add(combo)
                        count.clear()
                        score += 2
                
                if sum(count) > 15:
                    count.clear()
            print(score)
        generate_hand()
        count(hand, loop_count)

CribbageCalc.novel_count()