import random

class CribbageCalc:
    def generate_hand():
        #List out suits and values
        suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        #Create deck using comprehension of suits and values
        deck = [f'{v} of {s}' for s in suits for v in values]

        #Define quanitity of cards to be counted (6 total including flip after crib discard)
        quantity = 6
        hand = []
        hand_len = len(hand)
        
        while hand_len < quantity:
            card = deck[random.randint(0,51)]
            if card not in hand:
                hand.append(card)
                hand_len = len(hand)
        print(hand)

        #Ask to count 15s
        verify = input("Count 15s? Y or N ")
        if verify == 'Y' or verify == 'y':
            CribbageCalc.count_15s(hand, quantity)
        else:
            print('Done')

    def count_15s(hand, quantity):
        #Count values by adding to list and operating
        val_lst = []
        n = 0
        #Create list of values to add
        for i in range(quantity):
            #Grab the card
            info = hand[n]
            #Move to the next card for next iteration
            n += 1
            #Isolate value from card info and select
            value = info.split(' of')[0]
            if value == 'Jack' or value == 'Queen' or value == 'King':
                val_lst.append(10)
            elif value == 'Ace':
                val_lst.append(1)
            else:
                val_lst.append(int(value))
        print(val_lst)

CribbageCalc.generate_hand()