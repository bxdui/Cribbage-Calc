import random
import itertools
import collections

# Goals: start card, nibs/nobs, ease of input for pre-determined hand, flushes, runs, pairs/multiples

class CribbageCalc:
    def calculate():
        def gen_hand(quantity=5):
            # A list of single-character suits and values will be combined into a list to create a 52-card deck
            suits = ['C', 'S', 'H', 'D']
            values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

            # Construct deck as nested list of [hand, value]: v to track number values and s to track suits 
            deck = [[v, s] for s in suits for v in values]

            # quantity defines how many cards are to be placed in the hand
            #quantity = 4

            # Define hand as a list to represent the hand of cards
            hand = []

            # Define hand_len as a check to match with quantity, ensuring the loop will continue until the number of
            # cards in the hand equals the quantity variable. hand_len will be defined outside of the loop as an integer
            hand_len = len(hand)

            while hand_len < quantity:
                # Define card as one of any elements from list deck
                card = deck[random.randint(0,51)]
                # Ensure the chosen card is not a duplicate and add it to the hand
                if card not in hand:
                    hand.append(card)
                    # hand_len is updated on each loop to ensure proper loop count
                    hand_len = len(hand)

            print(hand)
            count(hand)

        def count(hand):
            print('Calculating score...')
            # Define score as int to track score
            score = 0
            # Define hand_val to track string values to convert to int (J, Q, K)
            hand_val = []
            # Define n2 as int for iteration in hand
            n2 = 0
            for i in range(len(hand)):
                # For each card in hand, check value if type is a string
                value = hand[n2][0]
                if value.upper() == 'J' or value.upper() == 'Q' or value.upper() == 'K':
                    # If value is a letter, operate on value 10
                    hand_val.append(10)
                else:
                    # Otherwise, convert the value to int
                    hand_val.append(int(value))
                # Update n to operate on the next card in the next loop
                n2 += 1

            # Define scorecard as a list. fifteens is a tuple that includes identified values that add to 15. Range +1 to account for full hand
            scorecard = [fifteens for i in range(len(hand_val) + 1) for fifteens in itertools.combinations(hand_val, i) if sum(fifteens) == 15]
            print(f'Fifteens identified: {scorecard}')

            # For every value added to scorecard (added per fifteen found), add two to the score
            for i in range(len(scorecard)):
                print('Fifteen, +2')
                score += 2

            # Create a list suits to display all suits in hand
            suits = [suit for card in hand for suit in card[1]]
            for suit in suits:
                # Take first suit, see if there are more than three instances. Runs will always appear in the first suit, no need to identify others
                s_quant = suits.count(suits[0])
                if s_quant > 3:
                    # Add number of cards in run. This will not work for start card addition
                    score += s_quant
                    break
                else:
                    pass

            # Finally, display the score
            print(f'Your hand is worth {score} points.')

        verify1 = input('How many cards in hand (including start card, 5 assumed)? ')

        verify2 = input('Enter hand as: ex. King of Clubs, Ace of Clubs as: K C, 1 C or R for random: ')
        if verify2.upper() == 'R':
            gen_hand()
        else:
            n1 = 0
            pd_card = verify2.split(', ')
            pd_hand = []
            for i in range(int(verify1)):
                pd_hand.append(pd_card[n1].split(' '))
                n1 += 1
            print(pd_hand)
            count(pd_hand)
    
CribbageCalc.calculate()