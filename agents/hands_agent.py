import random
from model.card import Card
from model.deck import Deck


class HandAgent(object):
    def __init__(self, deck):
        self.deck = deck
