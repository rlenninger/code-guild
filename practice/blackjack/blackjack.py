"""This is a blackjack game that calls on class modules."""

from card import Card
from deck import Deck
from deck import initialize_deck
from deck import shuffle_deck
from deck import draw_card_from_deck
from deck import check_for_empty_deck
from hand import Hand
from hand import add_card_to_hand
from hand import score_hand

SUITS = ['C', 'D', 'H', 'S']
RANK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']

def set_up_game():
    """Begins a round of Blackjack with the player by creating and shuffling a deck and dealing 2 cards to start."""
    deck = initialize_deck(SUITS, RANK)
    shuffle_deck(deck)
    active_hand = []
    active_hand += [draw_card_from_deck(deck)]
    active_hand += [draw_card_from_deck(deck)]
    # print(active_hand)
    print('Howdy, They call me the Gambler and we\'re going to play a game of Blackjack.\n'
          'Looks like your current hand is: ' + str(active_hand) + '\n'
          'That would make your score, ' + str(score_hand(active_hand)) + '.')
    print(str(hit_or_stand(active_hand, deck)))


def hit_or_stand(active_hand, deck):
    """Asks player if they would like to hit or stand.


    """
    player_choice = input('Would you like to hit or stand? ')
    if player_choice == 'hit':
        active_hand += [draw_card_from_deck(deck)]
    else:
        score_hand(active_hand)


def win_or_bust(active_hand):
    if active_hand < 22:
        print('You gotta know when to walk away, that hand is a bust.')
    elif active_hand == 21:
        print('21, that\'s BlackJack! You Win!')
    else:
        print(str(score_hand(active_hand)) + ', that\'s a fine score. You clearly know when to hold \'em')



def main():
    game_start = set_up_game()

if __name__ == '__main__':
    main()
