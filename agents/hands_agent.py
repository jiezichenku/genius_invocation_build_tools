import random
import copy
from model.card import Card
from model.deck import Deck


class HandAgent(object):
    def __init__(self, deck):
        self.deck = deck
        self.random_deck_list = []

    def generate_random_decks(self, n):
        l = list(range(self.deck.deck_size))
        print(l)
        unique_perms = set()

        while len(unique_perms) < n:
            # 生成一个随机排列
            perm = tuple(random.sample(l, self.deck.deck_size))
            unique_perms.add(perm)

        for perm in list(unique_perms):
            tmp_deck = copy.deepcopy(self.deck)
            tmp_deck.cards = [self.deck.cards[i] for i in perm]
            self.random_deck_list.append(tmp_deck)

