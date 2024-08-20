from data.data_loader import get_info_by_share_id


class Card(object):
    def __init__(self, share_id):
        self.data = get_info_by_share_id(share_id)
        self.id = self.data["id"]
        self.share_id = self.data["shareId"]
        self.name = self.data["name"]
        self.english_name = self.data["englishName"]
        # self.image = get_image(self.id)
        self.play_cost = self.data["playCost"]
        self.is_legend = False
        if "GCG_TAG_LEGEND" in self.data["tags"]:
            self.is_legend = True
        self.valuable = False
        self.playable = False

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return self.id == other.id
