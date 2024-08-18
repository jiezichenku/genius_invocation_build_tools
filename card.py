class Card(object):
    def __init__(self, cid, valid):
        self.id = cid
        self.valid = valid

    def __str__(self):
        if self.valid:
            return "%s_v" % self.id
        else:
            return "%s_i" % self.id

    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return self.id == other.id
