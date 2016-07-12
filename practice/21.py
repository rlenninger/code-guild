"""
Gives black jack advice.
"""
# setup
FACE_CARDS = ['j', 'q', 'k']
print('Hi! I am a bot that can give you blackjack advice.')

# input, get cards and assign values
print('What is your first card? ')
card_one = input()

print('What is your second card? ')
card_two = input()
# assign values
if card_one in FACE_CARDS:
    card_one_value = 10
elif card_one == 'a':
    card_one_value = 1
else:
    card_one_value = int(card_one)

if card_two in FACE_CARDS:
    card_two_value = 10
elif card_two == 'a':
    card_two_value = 1
else:
    card_two_value = int(card_two)

# transform, add values together
hand_value = card_one_value + card_two_value
# factor for a being 1 or 11
if card_one_value == 1:
    if hand_value <= 11:
        hand_value = hand_value + 10

if card_two_value == 1:
    if hand_value <= 11:
        hand_value = hand_value + 10

# output
print('Your hand value is ' + str(hand_value))
if hand_value == 21:
    print('Blackjack! A winner is you!')
elif hand_value < 17:
    print('You should hit!')
elif hand_value >= 17:
    print('You should stand!')
