import random
import sys

class Player:
    """
    A human player for blackjack
    """
    def __init__(self, game):

        """
        Constructs a player with the necessary features
        """
        # self.hand = hand() # For when we treat cards as objects
        self.game = game
        self.total = 0
        self.card1 = 0
        self.card2 = 0
        self.hits = 0
        self.funds = 100

    def start(self):
        """
        Draws the player's initial hand and checks it for blackjack
        """
        self.card1 = random.randint(2, 11)
        self.card2 = random.randint(1, 10)

        if self.card1 == 10 and self.card2 == 1:  # Forgot about drawing a "10" then a "1" - this fixes it
            self.card2 = 11 #ST: I don't follow the logic here, but it seems to work

        print("Here are your cards")
        print("Card 1 =", str(self.card1))
        print("Card 2 =", str(self.card2))

        self.total = self.card1 + self.card2 
        # There's a better way to do this...right?
        #ST: I think that's pretty good. Nothing clever I can think of.

        print("Your current total is", str(self.total))
        if self.total == 21:
            print("Blackjack! You win!")
            sys.exit()
        input("Press Enter to continue...")

    def play(self):
        """
        Allow the player to chose to hit or stand
        """
        while True:
            #ST: Let's save some work copy and pasting!
            #ST: You can use compound logic statments in if, to require less "elif" blocks
            #ST: An even better way to parse user input is to find out what python's version of a toLowerCase(str) function is, and force all input to lower case. Then you catch Hit and hit and HIt etc just by testing against "hit"
            hitStand = str(input("Hit or Stand? "))
            if hitStand == "stand" or hitStand =="Stand":
                break
            # elif hitStand == "Stand":
            # break
            elif hitStand == "hit" or hitStand == "Hit":
                hitCard = random.randint(1,10)
                self.total = self.total + hitCard
                #ST: An alternate way to write the line above:
                # self.totalt += hitCard
                #ST: the += operator means "add this to it and set the sum as the new value"
                #ST: It's basically a style preference though
                self.hits = self.hits + 1
                # self.hits += 1

                print("You drew a", str(hitCard))
                print("Your total is", str(self.total))
                #input("Press Enter to continue...")

                #ST: If you reorder these next two blocks to bust first, you can skip the "and self.total < 22" statement.
                if self.hits >= 3 and self.total < 22:
                    print("5 cards drawn. You win!")
                    break
                    #ST: I think you might want exit instead of break, because I think this still lets you lose to the dealer on value after drawing 5. I know the draw 5 thing is leaving the game anyway.
                if self.total > 21:
                    print("Busted!")
                    sys.exit()
            # elif hitStand == "Hit":
            #     hitCard = random.randint(1,10)
            #     self.total = self.total + hitCard
            #     self.hits = self.hits + 1
            #     print("You drew a", str(hitCard))
            #     print("Your total is", str(self.total))
            #     #input("Press Enter to continue...")
            #     if self.hits >= 3 and self.total < 22:
            #         print("5 cards drawn. You win!")
            #         break
            #     if self.total > 21:
            #         print("Busted!")
            #         sys.exit()
            else:
                print("I didn't get that")
