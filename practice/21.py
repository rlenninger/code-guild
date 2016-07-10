"""
Gives black jack advice.
"""
# setup
print('Hi! I am a bot that can give you blackjack advice.')

# input, get cards and assign values
print('What is your first card? ')
card_one = str(input())

print('What is your second card? ')
card_two = str(input())
# assign values
if card_one == 'a':
    card_one = 1
elif card_one == 'ace':
    card_one = 1
elif card_one == 'A':
    card_one = 1
elif card_one == 'Ace':
    card_one = 1
elif card_one == '2':
    card_one = 2
elif card_one == '3':
    card_one = 3
elif card_one == '4':
    card_one = 4
elif card_one == '5':
    card_one = 5
elif card_one == '6':
    card_one = 6
elif card_one == '7':
    card_one = 7
elif card_one == '8':
    card_one = 8
elif card_one == '9':
    card_one = 9
elif card_one == '10':
    card_one = 10
elif card_one == 'j':
    card_one = 10
elif card_one == "J":
    card_one = 10
elif card_one == 'q':
    card_one = 10
elif card_one == 'Q':
    card_one = 10
elif card_one == 'k':
    card_one = 10
elif card_one == 'K':
    card_one = 10
# card_two values get assigned
if card_two == 'a':
    card_two = 1
elif card_two == 'A':
    card_two = 1
elif card_two == 'ace':
    card_two = 1
elif card_two == 'Ace':
    card_two = 1
elif card_two == '2':
    card_two = 2
elif card_two == '3':
    card_two = 3
elif card_two == '4':
    card_two = 4
elif card_two == '5':
    card_two = 5
elif card_two == '6':
    card_two = 6
elif card_two == '7':
    card_two = 7
elif card_two == '8':
    card_two = 8
elif card_two == '9':
    card_two = 9
elif card_two == '10':
    card_two = 10
elif card_two == 'j':
    card_two = 10
elif card_two == 'J':
    card_two = 10
elif card_two == 'q':
    card_two = 10
elif card_two == 'Q':
    card_two = 10
elif card_two == 'k':
    card_two = 10
elif card_two == 'K':
    card_two = 10

# transform, add values together
hand_value = card_one + card_two
# factor for a being 1 or 11
if card_one == 1:
    if hand_value < 10:
        hand_value = hand_value + 10
    elif hand_value == 10:
        hand_value = hand_value + 10
    elif hand_value == 11:
        hand_value = hand_value + 10
if card_two == 1:
    if hand_value < 10:
        hand_value = hand_value + 10
    elif hand_value == 10:
        hand_value = hand_value + 10
    elif hand_value == 11:
        hand_value = hand_value + 10

# output
print('Your hand value is ' + str(hand_value))
if hand_value == 21:
    print('Blackjack! A winner is you!')
elif hand_value < 17:
    print('You should hit!')
elif hand_value >= 17:
    print('You should stand!')
