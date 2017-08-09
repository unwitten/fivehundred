"""
Classic to represent basic objects like cards, bids and players.
"""
from collections import namedtuple
from enum import Enum
from itertools import cycle
from typing import Iterable, List, Union

MAX_PLAYER_HAND_SIZE = 10


class CardSuit(Enum):
    Spades = 'Spades'
    Clubs = 'Clubs'
    Diamonds = 'Diamonds'
    Hearts = 'Hearts'


class CardValue(Enum):
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


class BidType(Enum):
    Spades = 'Spades'
    Clubs = 'Clubs'
    Diamonds = 'Diamonds'
    Hearts = 'Hearts'
    NoTrumps = 'No Trumps'
    Misere = 'Misere'
    OpenMisere = 'Open Misere'


BASE_BID_VALUES = {
    BidType.Spades: 40,
    BidType.Clubs: 60,
    BidType.Diamonds: 80,
    BidType.Hearts: 100,
    BidType.NoTrumps: 120,
}


class PlayerHandSizeError(Exception):
    pass


# lightweight object to hold information about a card
class Card(namedtuple("Card", ["value", "suit"])):
    __slots__ = ()

    def __str__(self):
        # Special case because the joker doesn't have a suit?
        if self.value == CardValue.Joker:
            return self.value.value

        return f"{self.value.value} of {self.suit.value}"


# lightweight object to hold information about a bid
class Bid(namedtuple("Bid", ["number", "bid_type", "points"])):
    __slots__ = ()

    def __str__(self):
        # Special case when Misere
        if self.bid_type in {BidType.Misere, BidType.OpenMisere}:
            return f"{self.bid_type.value} ({self.points})"

        return f"{self.number} {self.bid_type.value} ({self.points})"


# lightweight object to hold information about a player
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: List[Card] = []

    def __str__(self):
        return self.name

    def reset_hand(self):
        """
        Reset a player's hand to be empty for the next round of dealing.
        """
        self.hand = []

    def give_card(self, card: Card):
        """
        Add a card to the players hand.

        Raise an exception if the player already has a full hand.
        """
        if len(self.hand) >= MAX_PLAYER_HAND_SIZE:
            raise PlayerHandSizeError("{self.name} has a full hand")
        else:
            self.hand.append(card)


def suit_is_red(suit: CardSuit):
    if suit in {CardSuit.Diamonds, CardSuit.Hearts}:
        return True
    return False


def card_is_red(card: Card):
    return suit_is_red(card.suit)


def gen_game_deck():
    for value in CardValue:
        # Special case for Joker
        if value == CardValue.Joker:
            yield Card(value, None)
            continue

        for suit in CardSuit:
            # Only red suits contain 4's
            if value == CardValue.Four and not suit_is_red(suit):
                continue
            yield Card(value, suit)


def get_bid_points(bid_type: BidType, number: Union[int, float]):
    # Special case for Misere and OpenMisere
    if bid_type == BidType.Misere:
        return 250
    if bid_type == BidType.OpenMisere:
        return 500

    # Return base value + 100 for each number over 6
    return BASE_BID_VALUES[bid_type] + 100 * (number - 6)


def gen_all_bids():
    for bid_type in BidType:
        # Special case for Misere and OpenMisere
        if bid_type in {BidType.Misere, BidType.OpenMisere}:
            yield Bid(number=None, bid_type=bid_type, points=get_bid_points(bid_type, None))
            continue

        # Cover all bids from 6 to 10
        for number in range(6, 11):
            yield Bid(number=number, bid_type=bid_type, points=get_bid_points(bid_type, number))


def deal_cards(players: List[Player], deck: Iterable[Card]):
    """
    Deal cards from a full deck to the players until their hands are full. Returns the remaining cards.

    Assumes the deck has already been shuffled.
    """
    kitty = list()
    for player, card in zip(cycle(players), deck):
        try:
            player.give_card(card)
        except PlayerHandSizeError:
            kitty.append(card)

    return kitty
