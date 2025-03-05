class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Add a card (tuple) to the hand."""
        self.cards.append(card)

    def display(self):
        """Return a string representation of the hand."""
        return ", ".join([f"{rank} of {suit}" for rank, suit in self.cards])

    def count(self):
        """Return the number of cards in the hand."""
        return len(self.cards)
