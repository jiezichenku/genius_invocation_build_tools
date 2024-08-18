import base64
from typing import List
import random
import json


deck_code_data = json.load(
    open("data/deck_code_data.json")
)

name_map = deck_code_data["name_map"][:]
forbid_list = deck_code_data["forbid_list"][:]
characters_idx = []
for i in range(len(name_map)):
    if name_map[i].startswith("character:"):
        characters_idx.append(i)
        name_map[i] = name_map[i][10:]


def deck_code_to_deck_str(deck_code: str, version: str | None = None) -> list:
    """
    Convert the base64 deck code to deck str. If version is set, add
    default_version.
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
        decode.append(int(res[i : i + 12], 2))
    decode = decode[:-1]
    results = []
    if version is not None:
        results.append(f"default_version:{version}")
    for x in decode:
        results.append(x)
    return results


if __name__ == "__main__":
    deck = "AjEyyo0NApFh31APGTHx5JgPCkFy5TUQFEFB9b0QDFHB98IQDWISljcaFGJhDMQRDbEB"
    x = deck_code_to_deck_str(deck)
    print(x)
