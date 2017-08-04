from fivehundred.base import Card


def test_card_string():
    """Test that str(card) works as expected."""
    assert str(Card(value="Jack", suit="Spades")) == "Jack of Spades"
