import random

suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [f'{v} of {s}' for s in suits for v in values]
quantity = 5

class CribbageCalc:
    def generate_hand():
        # quantity = 5
        hand = []
        hand_len = len(hand)
        while hand_len < quantity:
            card = deck[random.randint(0,51)]
            if card not in hand:
                hand.append(card)
                hand_len = len(hand)
        print(hand)

        verify = input("Count 15's? Y or N ")

        if verify == 'Y' or verify == 'y':
            val_lst = []
            n = 0
            for i in range(quantity):
                info = hand[n]
                n += 1
                value = info.split(' of')[0]
                if value == 'Jack' or value == 'Queen' or value == 'King':
                    val_lst.append(10)
                elif value == 'Ace':
                    val_lst.append(1)
                else:
                    val_lst.append(int(value))
            print(val_lst)
        else:
            print('Done')         

CribbageCalc.generate_hand()