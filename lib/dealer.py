import random
import sys

class Dealer :
    """
    A computer dealer for blackjack
    """
    def __init__(self, game):
        """
        Constructs a dealer with the necessary features
        """
        # self.hand = hand() # For when we treat cards as objects
        self.game = game #ST: Back references like this let us talk back to other components of the "game" object, in this case the player
        self.total = 0
        self.card1 = 0
        self.card2 = 0
        self.hits = 0

    def start(self):
        """
        Draws the dealer's initial hand and checks it for blackjack
        """
        self.card1 = random.randint(2,11)
        self.card2 = random.randint(1,10)

        if self.card1 == 10 and self.card2 == 1:
            self.card2 = 11 #ST: I don't follow the logic here, but it seems to work

        self.total = self.card1 + self.card2

        if self.total == 21:
            print("Dealer Blackjack! You lose!")
            sys.exit()

    def play(self):
        """
        Makes the dealer hit or stand as appropriate
        """
        if self.total == self.game.player.total: #ST: I think the standard rule is the dealer will hit on a push, if under 17, so move this down?
            print("Push (tied).")
            sys.exit()
        elif self.total > self.game.player.total: #ST: I think the dealer hits here too, if under 17
            print("Your total is", str(self.game.player.total))
            print("The dealer has", str(self.total))
            print("The dealer wins.")
            sys.exit()
        else:
            while self.total < 17:
                input("The dealer hits. (Press Enter to continue...)")
                hitCard = random.randint(1,10)
                print("The dealer draws a", str(hitCard))
                self.total = self.total + hitCard
                print("The dealer now has", str(self.total))
                #input("Press Enter to continue...")
                if self.total > 21:
                    print("Dealer busts. You win!")
                    sys.exit()
