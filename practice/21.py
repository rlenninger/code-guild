"""A simple program that gives blackjack advice."""
# setup
FACE_CARDS = ['j', 'q', 'k']

def assign_card_one():
	"""Asks for first card and assigns num value."""
	card_one = input('What is your first card? ')
	if card_one in FACE_CARDS:
		card_one_value = 10
	elif card_one == 'a':
		card_one_value = 1
	else:
		card_one_value = int(card_one)
	return card_one_value

def assign_card_two():
	"""Asks for second card and assigns num value."""
	card_two = input('What is your second card? ')
	if card_two in FACE_CARDS:
		card_two_value = 10
	elif card_two == 'a':
		card_two_value = 1
	else:
		card_two_value = int(card_two)
	return card_two_value

def assign_hand_value(card_one_hand_value, card_two_hand_value):
	"""Sums hand value and decides if 'a' should be 1 or 11."""
	hand_value = card_one_hand_value + card_two_hand_value
	if card_one_hand_value == 1:
		if hand_value <= 11:
			hand_value = hand_value + 10
	if card_two_hand_value == 1:
		if hand_value <= 11:
			hand_value = hand_value + 10
	return hand_value

def main():
	"""Calls functions and outputs results."""
	card_one_value = assign_card_one()
	card_two_value = assign_card_two()
	output = assign_hand_value(card_one_value, card_two_value)
	output_value = output
	print('Your hand value is ' + str(output_value))
	if output_value == 21:
		print('Blackjack! A winner is you!')
	elif output_value < 17:
		print('You should hit!')
	elif output_value >= 17:
		print('You should stand!')

main()