"""
Classic to represent basic objects like cards.
"""
from collections import namedtuple


# lightweight object to hold information about a person
class Card(namedtuple("Card", ["value", "suit"])):
    __slots__ = ()

    def __str__(self):
        # Special case because the joker doesn't have a suit?
        if self.value == "Joker":
            return self.value

        return "{} of {}".format(self.value, self.suit)  # f strings where are you?
