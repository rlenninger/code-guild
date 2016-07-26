"""
Deck value class that can: return a new deck that is shuffled, draw a card off the top of the deck,
return if deck is empty.
"""
from card import Card
from random import shuffle
SUITS = ['C', 'D', 'H', 'S']
RANK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']


class Deck:
    """A class for Deck."""
    def __init__(self, list_of_cards):
        self.list_of_cards = list_of_cards


    def __repr__(self):
        """Returns repr."""

        return 'Deck({!r})'.format(self.list_of_cards)


    def __eq__(self, other):
        """Checks to see if eq.

        >>> (Deck([Card('S', 'A'), Card('D', 'J')])) == (Deck([Card('S', 'A'), Card('D', 'J')]))
        True
        >>> (Deck([Card('S', 'A'), Card('D', 'J')])) == (Deck([Card('D', 'A'), Card('C', 'J')]))
        False
        """
        return self.list_of_cards == other.list_of_cards


def initialize_deck(suits, rank):
    """Returns a sorted deck."""
    deck = Deck([])
    for suit in SUITS:
        for rank in RANK:
            deck.list_of_cards += [Card(suit, rank)]
    return deck


def shuffle_deck(deck):
    """Does the Truffle Shuffle and shuffles the deck."""
    shuffle(deck.list_of_cards)


def draw_card_from_deck(deck):
    """Draws a card from the deck with pop.

    >>> draw_card_from_deck(Deck([Card('S', 'A')]))
    Card('S', 'A')
    """
    return deck.list_of_cards.pop()


def check_for_empty_deck(deck):
    """Checks len count of deck and returns True or False.

    >>> check_for_empty_deck(Deck([]))
    True
    >>> check_for_empty_deck(Deck([Card('S', 'A'), Card('D', 'J')]))
    False
    """
    return len(deck.list_of_cards) == 0
