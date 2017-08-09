import pytest

from fivehundred.base import (
    Bid,
    BidType,
    Card,
    CardValue,
    CardSuit,
    Player,
    gen_all_bids,
)


@pytest.fixture
def fixture_player_empty_hand():
    return Player(name="Chang")


@pytest.fixture
def fixture_player_full_hand(fixture_player_empty_hand):
    player = fixture_player_empty_hand
    player.hand.append(Card(value=CardValue.Four, suit=CardSuit.Hearts))
    player.hand.append(Card(value=CardValue.Five, suit=CardSuit.Spades))
    player.hand.append(Card(value=CardValue.Six, suit=CardSuit.Clubs))
    player.hand.append(Card(value=CardValue.Seven, suit=CardSuit.Diamonds))
    player.hand.append(Card(value=CardValue.Eight, suit=CardSuit.Hearts))
    player.hand.append(Card(value=CardValue.Nine, suit=CardSuit.Spades))
    player.hand.append(Card(value=CardValue.Ten, suit=CardSuit.Clubs))
    player.hand.append(Card(value=CardValue.Jack, suit=CardSuit.Diamonds))
    player.hand.append(Card(value=CardValue.Queen, suit=CardSuit.Hearts))
    player.hand.append(Card(value=CardValue.Joker, suit=None))

    return player


@pytest.mark.parametrize(
    ("value", "suit", "expected_result"),
    [
        (CardValue.Jack, CardSuit.Spades, "Jack of Spades"),
        (CardValue.Joker, None, "Joker"),
    ],
    ids=[
        "standard_card",
        "joker",
    ],
)
def test_card_string(value, suit, expected_result):
    """Test that str(card) works as expected."""
    assert str(Card(value=value, suit=suit)) == expected_result


@pytest.mark.parametrize(
    ("number", "bid_type", "points", "expected_result"),
    [
        (6, BidType.Spades, 40, "6 Spades (40)"),
        (8, BidType.Hearts, 300, "8 Hearts (300)"),
        (10, BidType.NoTrumps, 520, "10 No Trumps (520)"),
        (None, BidType.Misere, 250, "Misere (250)"),
        (None, BidType.OpenMisere, 500, "Open Misere (500)"),
    ],
    ids=[
        "six_spades",
        "eight_hearts",
        "ten_no_trumps",
        "misere",
        "open_misere",
    ],
)
def test_bid_string(number, bid_type, points, expected_result):
    """Test that str(bid) works as expected."""
    assert str(Bid(number=number, bid_type=bid_type, points=points)) == expected_result


def test_gen_all_bids():
    """Test that gen_all_bids works as expected."""
    all_bids = list(gen_all_bids())

    assert all_bids == [
        Bid(number=6, bid_type=BidType.Spades, points=40),
        Bid(number=7, bid_type=BidType.Spades, points=140),
        Bid(number=8, bid_type=BidType.Spades, points=240),
        Bid(number=9, bid_type=BidType.Spades, points=340),
        Bid(number=10, bid_type=BidType.Spades, points=440),
        Bid(number=6, bid_type=BidType.Clubs, points=60),
        Bid(number=7, bid_type=BidType.Clubs, points=160),
        Bid(number=8, bid_type=BidType.Clubs, points=260),
        Bid(number=9, bid_type=BidType.Clubs, points=360),
        Bid(number=10, bid_type=BidType.Clubs, points=460),
        Bid(number=6, bid_type=BidType.Diamonds, points=80),
        Bid(number=7, bid_type=BidType.Diamonds, points=180),
        Bid(number=8, bid_type=BidType.Diamonds, points=280),
        Bid(number=9, bid_type=BidType.Diamonds, points=380),
        Bid(number=10, bid_type=BidType.Diamonds, points=480),
        Bid(number=6, bid_type=BidType.Hearts, points=100),
        Bid(number=7, bid_type=BidType.Hearts, points=200),
        Bid(number=8, bid_type=BidType.Hearts, points=300),
        Bid(number=9, bid_type=BidType.Hearts, points=400),
        Bid(number=10, bid_type=BidType.Hearts, points=500),
        Bid(number=6, bid_type=BidType.NoTrumps, points=120),
        Bid(number=7, bid_type=BidType.NoTrumps, points=220),
        Bid(number=8, bid_type=BidType.NoTrumps, points=320),
        Bid(number=9, bid_type=BidType.NoTrumps, points=420),
        Bid(number=10, bid_type=BidType.NoTrumps, points=520),
        Bid(number=None, bid_type=BidType.Misere, points=250),
        Bid(number=None, bid_type=BidType.OpenMisere, points=500),
    ]


def test_player():
    """Test that the Player class works as expected."""
    player = Player(name="Chang")

    assert player.hand == []
    assert player.name == "Chang"
    assert str(player) == "Chang"


def test_player_reset_hand(fixture_player_full_hand, fixture_player_empty_hand):
    """Test that player.reset_hand works as expected."""
    player = fixture_player_full_hand

    assert player.hand == [
        Card(value=CardValue.Four, suit=CardSuit.Hearts), Card(value=CardValue.Five, suit=CardSuit.Spades),
        Card(value=CardValue.Six, suit=CardSuit.Clubs), Card(value=CardValue.Seven, suit=CardSuit.Diamonds),
        Card(value=CardValue.Eight, suit=CardSuit.Hearts), Card(value=CardValue.Nine, suit=CardSuit.Spades),
        Card(value=CardValue.Ten, suit=CardSuit.Clubs), Card(value=CardValue.Jack, suit=CardSuit.Diamonds),
        Card(value=CardValue.Queen, suit=CardSuit.Hearts), Card(value=CardValue.Joker, suit=None),
    ]

    player.reset_hand()

    assert player.hand == fixture_player_empty_hand.hand == []
