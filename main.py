from utils.deck_code_loader import deck_code_to_deck_str
from model.deck import Deck
from agents.hands_agent import HandAgent

if __name__ == "__main__":
    deck = "EYCQyBwMA5BRySITEnEgOHETB4AQ3oMPCFAx9TMPE2Ax/jUPE+FhAzYQDDEgTMIUDMAA"
    deck = Deck(deck_code_to_deck_str(deck))
    a = HandAgent(deck)
    print(a.generate_random_decks(10))
