from collections import deque

suits = ['C', 'S', 'H', 'D']
values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
#Create deck using comprehension of suits and values
deck = [f'{v} of {s}' for s in suits for v in values]

# lst = [9, 3, 2, 1, 10]

'''
Step 1) Select a card from your hand to count with other cards

Step 2) Select an additional card until the sum of the selected cards is 15 (add 2 pts), >15, or exceeds the total cards in hand

NO repeat combinations

Continue until all possible combinations have been made
'''  

class CribbageCalc:
    def generate_hand():
        #List out suits and values
        suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
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
                suit = info.split('of ')[1]
                if value == 'Jack' or value == 'Queen' or value == 'King':
                    val_lst.append(10)
                elif value == 'Ace':
                    val_lst.append(1)
                else:
                    val_lst.append(int(value))
            print(val_lst)

        #Ask to count 15s
        # verify = input("Count 15s? Y or N ")
        # if verify == 'Y' or verify == 'y':
        #     CribbageCalc.count_15s(hand, quantity)
        # else:
        #     print('Done')

    # Step 1)
    def select_card():
        score = 0
        n = 0
        count = deque([])
        checklist = {}
        for i in range(5):

            def find_15():
                count.append(lst[n])
                n += 1
                count.append(lst[n])
                sum = count[0] + count[1]
                if sum == 15:
                    score += 2
                    checklist.append(f'{val1}{SUIT1}{val2}{SUIT2}')
                elif sum > 15:
                    checklist.append(f'{val1}{SUIT1}{val2}{SUIT2}')
                elif sum < 15:
                    count.append(lst[n+1])
                else:
                    print('poopoo')

select_card()