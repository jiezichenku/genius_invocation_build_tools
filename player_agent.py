import random
from card import Card


class Player_agent(object):
    def __init__(self, pair_num, valid_pair_num, valid_single_num, has_miracle, is_miracle_valid):
        self.deck_size = 30
        self.deck = []
        self.hand = []
        self.avoid = []
        self.has_miracle = has_miracle  # 是否包含秘传
        self.is_miracle_valid = is_miracle_valid  # 是否保留秘传
        self.pair_num = pair_num
        self.valid_pair_num = valid_pair_num
        self.single_num = self.deck_size - 2 * self.pair_num
        if self.has_miracle:
            self.single_num -= 1
        self.valid_single_num = valid_single_num
        if pair_num > self.deck_size / 2:
            raise Exception("Too much pairs, entity: %s" % self)
        if valid_pair_num > pair_num:
            raise Exception("Too much valid pair, entity: %s" % self)
        if valid_single_num > self.single_num:
            raise Exception("Too much valid single, entity: %s" % self)
        self.build_deck()

    def build_deck(self):
        if self.has_miracle:
            self.deck.append(Card(-1, self.is_miracle_valid))
        for i in range(self.valid_pair_num):
            self.deck.append(Card(i, True))
            self.deck.append(Card(i, True))
        for i in range(self.valid_pair_num, self.pair_num):
            self.deck.append(Card(i, False))
            self.deck.append(Card(i, False))
        for i in range(self.pair_num, self.pair_num + self.valid_single_num):
            self.deck.append(Card(i, True))
        for i in range(self.pair_num + self.valid_single_num, self.pair_num + self.single_num):
            self.deck.append(Card(i, False))
        if len(self.deck) != self.deck_size:
            raise Exception("deck size error, entity: %s" % self)

    def draw(self, num):
        pool = self.deck.copy()
        for i in self.avoid:
            for j in pool:
                if i == j:
                    pool.remove(j)
        self.avoid = []
        for i in range(num):
            to_draw = random.choice(self.deck)
            self.deck.remove(to_draw)
            self.hand.append(to_draw)

    def redraw(self):
        for i in self.hand:
            if not i.valid:
                self.deck.append(i)
                self.avoid.append(i)
        for i in self.avoid:
            self.hand.remove(i)
        self.draw(len(self.avoid))

    def valid_hand_num(self):
        ret = 0
        for i in self.hand:
            if i.valid:
                ret += 1
        return ret

    def __str__(self):
        return """
      self.deck = %s
      self.hand = %s
      self.has_merical = %s
      self.pair_num = %s
      self.valid_pair_num = %s
      self.single_num = %s
      self.valid_single_num = %s
      len(self.deck) = %s
      """ % (
            [x.__str__() for x in self.deck],
            [x.__str__() for x in self.hand],
            self.has_miracle,
            self.pair_num,
            self.valid_pair_num,
            self.single_num,
            self.valid_single_num,
            len(self.deck)
        )
