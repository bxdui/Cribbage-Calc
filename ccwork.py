import random
import itertools
from collections import deque

# Class defined to count paits, currently working on flushes

class CribbageCalc:
    def calculate():
        # A list of single-character suits and values will be combined into a list to create a 52-card deck
        suits = ['C', 'S', 'H', 'D']
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # Construct nested list of [hand, value]: v to track number values and s to track suits 
        deck = [[v, s] for s in suits for v in values]

        # quantity defines how many cards are to be placed in the hand
        quantity = 4

        # Define hand as a list to represent the hand of cards
        hand = []

        # Define hand_len as a check to match with quantity, ensuring the loop will continue until the number of
        # cards in the hand equals the quantity variable. hand_len will be defined outside of the loop as an integer
        hand_len = len(hand)
        
        while hand_len < quantity:
            card = deck[random.randint(0,51)]
            # Ensure the chosen card is not a duplicate and add it to the hand
            if card not in hand:
                hand.append(card)
                # hand_len is updated on each loop to ensure proper loop count
                hand_len = len(hand)

        print(hand)

        # Ask the user to count the points in their hand
        verify = input("Count hand? Y or N: ")
        
        if verify == 'Y' or verify == 'y':
            # Define score 
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

            # Define scorecard as a list. fifteens is a number that counts how many combinations equal fifteen
            scorecard = [fifteens for i in range(len(hand_val)) for fifteens in itertools.combinations(hand_val, i) if sum(fifteens) == 15]

            suits = [suit for card in hand for suit in card[1]]
            
            # For every value added to scorecard (added per fifteen found), add two to the score
            for i in range(len(scorecard)):
                score += 2
        else: 
            print('Done') 

        print(score)   

CribbageCalc.calculate()