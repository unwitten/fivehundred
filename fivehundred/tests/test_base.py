import pytest

from fivehundred.base import (
    Bid,
    BidTypes,
    Card,
    CardValues,
    CardSuits,
    gen_all_bids,
)


@pytest.mark.parametrize(
    ("value", "suit", "expected_result"),
    [
        (CardValues.Jack, CardSuits.Spades, "Jack of Spades"),
        (CardValues.Joker, None, "Joker"),
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
        (6, BidTypes.Spades, 40, "6 Spades (40)"),
        (8, BidTypes.Hearts, 300, "8 Hearts (300)"),
        (10, BidTypes.NoTrumps, 520, "10 No Trumps (520)"),
        (None, BidTypes.Misere, 250, "Misere (250)"),
        (None, BidTypes.OpenMisere, 500, "Open Misere (500)"),
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
        Bid(number=6, bid_type=BidTypes.Spades, points=40),
        Bid(number=7, bid_type=BidTypes.Spades, points=140),
        Bid(number=8, bid_type=BidTypes.Spades, points=240),
        Bid(number=9, bid_type=BidTypes.Spades, points=340),
        Bid(number=10, bid_type=BidTypes.Spades, points=440),
        Bid(number=6, bid_type=BidTypes.Clubs, points=60),
        Bid(number=7, bid_type=BidTypes.Clubs, points=160),
        Bid(number=8, bid_type=BidTypes.Clubs, points=260),
        Bid(number=9, bid_type=BidTypes.Clubs, points=360),
        Bid(number=10, bid_type=BidTypes.Clubs, points=460),
        Bid(number=6, bid_type=BidTypes.Diamonds, points=80),
        Bid(number=7, bid_type=BidTypes.Diamonds, points=180),
        Bid(number=8, bid_type=BidTypes.Diamonds, points=280),
        Bid(number=9, bid_type=BidTypes.Diamonds, points=380),
        Bid(number=10, bid_type=BidTypes.Diamonds, points=480),
        Bid(number=6, bid_type=BidTypes.Hearts, points=100),
        Bid(number=7, bid_type=BidTypes.Hearts, points=200),
        Bid(number=8, bid_type=BidTypes.Hearts, points=300),
        Bid(number=9, bid_type=BidTypes.Hearts, points=400),
        Bid(number=10, bid_type=BidTypes.Hearts, points=500),
        Bid(number=6, bid_type=BidTypes.NoTrumps, points=120),
        Bid(number=7, bid_type=BidTypes.NoTrumps, points=220),
        Bid(number=8, bid_type=BidTypes.NoTrumps, points=320),
        Bid(number=9, bid_type=BidTypes.NoTrumps, points=420),
        Bid(number=10, bid_type=BidTypes.NoTrumps, points=520),
        Bid(number=None, bid_type=BidTypes.Misere, points=250),
        Bid(number=None, bid_type=BidTypes.OpenMisere, points=500),
    ]
