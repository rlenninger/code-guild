"""
Class for Hand that can: add card to a hand, score a hand, return if score is over 21, allow user to type in a hand.
"""
from card import Card

FACE_CARDS = ['K', 'J', 'Q']
NUM_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']

class Hand:
    """A class for Hand"""
    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        """Returns repr."""
        return 'Hand({!r})'.format(self.card_list)

    def __eq__(self, other):
        """Checks to see if eq

       >>> Hand([Card('S', '2')]) == Hand([Card('D', '7')])
       False
       >>> Hand([Card('S', '2')]) == Hand([Card('S', '2')])
       True
        """
        return self.card_list == other.card_list

def add_card_to_hand(card, hand):
    """Adds a card to hand.

    >>> add_card_to_hand(Card('D', '7'), Hand([Card('S', '2')]))
    Hand([Card('S', '2'), Card('D', '7')])
    """

    hand.card_list += [card]
    return hand

def score_hand(hand):
    """Assigns point value to cards and scores hand.

    >>> score_hand(Hand([Card('S', '2'), Card('D', 'A')]))
    13
    >>> score_hand(Hand([Card('S', 'A'), Card('D', 'J')]))
    21
    >>> score_hand(Hand([Card('S', 'A'), Card('D', '9'), Card('C', '5')]))
    15
    >>> score_hand(Hand([Card('S', '9'), Card('D', '9'), Card('C', '5')]))
    23
    >>> score_hand(Hand([Card('S', '9'), Card('D', '9'), Card('C', 'A')]))
    19
    """
    hand_value = 0
    for card in hand:
        if card.rank in FACE_CARDS:
            hand_value += 10
        elif card.rank in NUM_CARDS:
            hand_value += int(card.rank)
        else:
            hand_value += 1
    for card in hand:
        if card.rank == 'A' and hand_value <= 11:
            hand_value += 10

    return hand_value
