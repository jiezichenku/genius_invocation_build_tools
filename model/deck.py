import random
from model.card import Card


class Deck(object):
    def __init__(self, card_list):
        self.deck_size = 30
        self.characters = card_list["characters"]
        self.cards = card_list["cards"]
        self.legend = []
        for card in self.cards:
            if card.is_legend:
                self.legend.append(card)
        self.hand = []
        self.avoid = []

    def draw(self, num):
        pool = self.cards.copy()
        for i in self.avoid:
            for j in pool:
                if i == j:
                    pool.remove(j)
        self.avoid = []
        for i in range(num):
            to_draw = random.choice(self.cards)
            self.cards.remove(to_draw)
            self.hand.append(to_draw)

    def redraw(self):
        for i in self.hand:
            if not i.valid:
                self.cards.append(i)
                self.avoid.append(i)
        for i in self.avoid:
            self.hand.remove(i)
            self.draw(len(self.avoid))

    def __str__(self):
        return f"characters: {[str(x) for x in self.characters]}, \ncards: {[str(x) for x in self.cards]}"
