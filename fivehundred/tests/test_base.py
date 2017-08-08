import pytest

from fivehundred.base import (
    Bid,
    BidTypes,
    Card,
    CardValues,
    CardSuits,
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
