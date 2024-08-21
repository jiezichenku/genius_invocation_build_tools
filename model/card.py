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
        self.value = 2  # 0: t1会留会打 1: t1不留会打 2: t1不留不打(default)
        self.draw_after_play = 0
        if self.id in [332004]:
            self.draw_after_play = 2
        if self.id in [332032]:
            self.draw_after_play = 4

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return self.id == other.id
