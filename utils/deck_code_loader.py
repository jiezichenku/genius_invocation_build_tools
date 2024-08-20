import base64
import json

from model.card import Card
from model.character import Character
from data.data_loader import get_deck_code_data

deck_code_data = get_deck_code_data()

name_map = deck_code_data["name_map"][:]
forbid_list = deck_code_data["forbid_list"][:]
characters_idx = []
for i in range(len(name_map)):
    if name_map[i].startswith("character:"):
        characters_idx.append(i)
    name_map[i] = name_map[i][10:]


def deck_code_to_deck_str(deck_code):
    """
    Convert the base64 deck code to card.
    """
    binary = base64.b64decode(deck_code)
    bb = []
    for b in binary:
        bb.append((256 + b - binary[-1]) % 256)
    bb = bb[:-1]
    binary = bb[::2] + bb[1::2]
    res = ""
    for i in binary:
        res += "{:08b} ".format(i)
    res = res.replace(" ", "")
    decode = []
    for i in range(0, len(res), 12):
        decode.append(int(res[i: i + 12], 2))
    decode = decode[:-1]
    results = {"characters": [], "cards": []}
    for x in decode:
        if 0 < x <= len(name_map):
            if x - 1 in characters_idx:
                results["characters"].append(Character(x))
        else:
            results["cards"].append(Card(x))
    return results
