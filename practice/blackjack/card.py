"""Class for all cards as strings."""

class Card:
    """Class for cards."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """Returns repr.

        >>> Card('D', 'K')
        Card('D', 'K')
        """

        return 'Card({!r}, {!r})'.format(self.suit, self.rank)

    def __eq__(self, other):
        """Checks to see if eq.

        >>> Card('D', 'K') == Card('D', 'K')
        True
        >>> Card('D', 'K') == Card('D', '7')
        False
        """

        return self.suit == other.suit and self.rank == other.rank



