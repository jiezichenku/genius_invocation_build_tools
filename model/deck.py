import random
from model.card import Card


class Deck(object):
    def __init__(self, card_list):
        self.characters = card_list["characters"]
        self.cards = card_list["cards"]
        self.deck_size = len(self.cards)
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
            to_draw = self.cards[0]
            self.cards.remove(to_draw)
            self.hand.append(to_draw)

    def redraw(self):
        for i in self.hand:
            if not i.valid:
                random_index = random.randint(0, len(self.cards))
                self.cards.insert(random_index, i)
                self.avoid.append(i)
        for i in self.avoid:
            self.hand.remove(i)
            self.draw(len(self.avoid))

    def set_value(self, cid, value):
        for i in self.cards:
            if i.id == cid:
                i.value = value

    def shuffle_by_index_list(self, index_list):
        self.cards = [self.cards[i] for i in index_list]

    def __str__(self):
        return f"characters: {[str(x) for x in self.characters]}, \ncards: {[str(x) for x in self.cards]}"

    def __eq__(self, other):
        return self.cards == other.cards
