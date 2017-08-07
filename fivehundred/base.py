"""
Classic to represent basic objects like cards, bids and players.
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


class BidTypes(Enum):
    Spades = 'Spades'
    Clubs = 'Clubs'
    Diamonds = 'Diamonds'
    Hearts = 'Hearts'
    NoTrumps = 'NoTrumps'
    Misere = 'Misere'
    OpenMisere = 'OpenMisere'


BASE_BID_VALUES = {
    BidTypes.Spades: 40,
    BidTypes.Clubs: 60,
    BidTypes.Diamonds: 80,
    BidTypes.Hearts: 100,
    BidTypes.NoTrumps: 120
}


# lightweight object to hold information about a card
class Card(namedtuple("Card", ["value", "suit"])):
    __slots__ = ()

    def __str__(self):
        # Special case because the joker doesn't have a suit?
        if self.value == CardValues.Joker:
            return self.value.value

        return f"{self.value.value} of {self.suit.value}"


# lightweight object to hold information about a bid
class Bid(namedtuple("Bid", ["bid_type", "number", "points"])):
    __slots__ = ()

    def __str__(self):
        # Special case when Misere
        if self.bid_type in {BidTypes.Misere, BidTypes.OpenMisere}:
            return f"{self.bid_type.value} ({self.points})"

        return f"{self.number} {self.bid_type.value} ({self.points})"


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name


def suit_is_red(suit: CardSuits):
    if suit in {CardSuits.Diamonds, CardSuits.Hearts}:
        return True
    return False


def card_is_red(card: Card):
    return suit_is_red(card.suit)


def gen_game_deck():
    for value in CardValues:
        # Special case for Joker
        if value == CardValues.Joker:
            yield Card(value, None)
            continue

        for suit in CardSuits:
            # Only red suits contain 4's
            if value == CardValues.Four and not suit_is_red(suit):
                continue
            yield Card(value, suit)


def get_bid_points(bid_type, number):
    # Special case for Misere and OpenMisere
    if bid_type == BidTypes.Misere:
        return 250
    if bid_type == BidTypes.OpenMisere:
        return 500

    # Return base value + 100 for each number over 6
    return BASE_BID_VALUES[bid_type] + 100*(number-6)


def gen_all_bids():
    for bid_type in BidTypes:
        # Special case for Misere and OpenMisere
        if bid_type in {BidTypes.Misere, BidTypes.OpenMisere}:
            yield Bid(bid_type, None, get_bid_points(bid_type, None))
            continue

        # Cover all bids from 6 to 10
        for number in range(6,11):
            yield Bid(bid_type, number, get_bid_points(bid_type, number))
