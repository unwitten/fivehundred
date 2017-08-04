"""
Classic to represent basic objects like cards.
"""
from collections import namedtuple
from enum import Enum


class CardSuits(Enum):
    Spades = 'Spades'
    Clubs = 'Clubs'
    Diamonds = 'Diamonds'
    Hearts = 'Hearts'


class CardValues(Enum):
    Four = 'Four'
    Five = 'Five'
    Six = 'Six'
    Seven = 'Seven'
    Eight = 'Eight'
    Nine = 'Nine'
    Ten = 'Ten'
    Jack = 'Jack'
    Queen = 'Queen'
    King = 'King'
    Ace = 'Ace'
    Joker = 'Joker'


# lightweight object to hold information about a person
class Card(namedtuple("Card", ["value", "suit"])):
    __slots__ = ()

    def __str__(self):
        # Special case because the joker doesn't have a suit?
        if self.value == CardValues.Joker:
            return self.value.value

        return "{} of {}".format(self.value.value, self.suit.value)  # f strings where are you?


def suit_is_red(suit):
    if suit in {CardSuits.Diamonds, CardSuits.Hearts}:
        return True
    return False


def gen_game_deck():
    for value in CardValues:
        # Special case for Joker
        if value == CardValues.Joker:
            yield Card(value, None)
            continue

        for suit in CardSuits:
            # Only red suits contain 4's
            if value == CardValues.Four:
                if not suit_is_red(suit):
                    continue
            yield Card(value, suit)
