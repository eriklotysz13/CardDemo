import pytest
from hand import Hand

def test_add_and_count():
    hand = Hand()
    # Initially the hand should be empty.
    assert hand.count() == 0, "Hand should initially have 0 cards"
    # Add two cards.
    hand.add_card(('Ace', 'Spades'))
    hand.add_card(('10', 'Hearts'))
    assert hand.count() == 2, "Hand should have 2 cards after adding two cards"

def test_display():
    hand = Hand()
    # Add a couple of cards.
    hand.add_card(('Queen', 'Diamonds'))
    hand.add_card(('3', 'Clubs'))
    display_str = hand.display()
    # Check that the display string contains the proper card descriptions.
    assert "Queen of Diamonds" in display_str, "Display should include 'Queen of Diamonds'"
    assert "3 of Clubs" in display_str, "Display should include '3 of Clubs'"
