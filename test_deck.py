import pytest
from deck import Deck

def test_generate_deck():
    deck = Deck()
    # Check that a new deck has 52 cards.
    assert len(deck.cards) == 52, "Deck should have 52 cards initially"

def test_shuffle_deck():
    deck = Deck()
    original_deck = deck.cards.copy()
    deck.shuffle()
    # After shuffling, the deck should still have the same cards (order might change).
    assert sorted(deck.cards) == sorted(original_deck), "Shuffled deck should contain the same cards"

def test_draw_card():
    deck = Deck()
    initial_count = len(deck.cards)
    card = deck.draw()
    # Check that drawing returns a card and that the deck has one fewer card.
    assert card is not None, "Drawing a card should return a card"
    assert len(deck.cards) == initial_count - 1, "Deck should have one less card after drawing"
