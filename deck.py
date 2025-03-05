import random

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        """Generate a full deck of 52 cards."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        # Create a list of tuples (rank, suit) for each card.
        return [(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw(self):
        """Draw a card from the deck.
        
        Returns:
            A card tuple (rank, suit) if available; otherwise, None.
        """
        if self.cards:
            return self.cards.pop()
        return None
