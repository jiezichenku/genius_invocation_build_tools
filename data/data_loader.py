import json
import os
from utils.request import get_image

ACTION_CARDS_DATA = "action_cards.json"
CHARACTERS_DATA = "characters.json"
DECK_CODE_DATA = "deck_code_data.json"
current_dir = os.path.dirname(__file__)
action_cards_file_path = os.path.join(current_dir, ACTION_CARDS_DATA)
characters_file_path = os.path.join(current_dir, CHARACTERS_DATA)
deck_code_data = os.path.join(current_dir, DECK_CODE_DATA)

with open(action_cards_file_path, encoding="utf-8") as f:
    action_cards = json.load(f)
    # for action_card in action_cards:
    #     cid = action_card["id"]
    #     cname = action_card["name"]
    #     img = get_image(cid)
    #     img.save(f"../img/cards/{cid}_{cname}.png")

with open(characters_file_path, encoding="utf-8") as f:
    characters = json.load(f)
    # for action_card in characters:
    #     cid = action_card["id"]
    #     cname = action_card["name"]
    #     img = get_image(cid)
    #     img.save(f"../img/characters/{cid}_{cname}.png")


def get_info_by_share_id(share_id):
    for action_card in action_cards:
        if action_card.get("shareId") == share_id:
            return action_card

    for character in characters:
        if character.get("shareId") == share_id:
            return character


def get_deck_code_data():
    return json.load(
        open(deck_code_data)
    )
