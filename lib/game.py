from lib.player import Player
from lib.dealer import Dealer

class Game:
    """
    A class to contain all the components of a game of blackjack
    """

    def __init__(self):
        """
        Initiates a Game object with the necessary features
        """
        self.dealer = Dealer(self) # The dealer
        self.player = Player(self) # The players: eventually change this to a list of players to allow for more than one
        # self.shoe = Shoe()       # When we implement the list for storing cards, we'll need this
