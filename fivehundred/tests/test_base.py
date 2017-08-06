import pytest

from fivehundred.base import Card, CardValues, CardSuits


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
