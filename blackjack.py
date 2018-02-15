#ST: We no longer need the random and sys imports because of restructuring
#ST: Notice the import below: I'm importing the "Game" class from the folder "lib" and file "game.py"
from lib.game import Game

def main():
    """
    Play a game of blackjack against the computer
    """
    #ST: Note the comment such as the one above which is put as the first statement of a function will automatically go in the 'doc' field of that function. It is the preferred style for function description comments
    #ST: Good practice is to wrap all commands in a "main" function

    game = Game()
    #ST: I stored our player and dealer objects inside a "game" object. This technique lets them talk to each other without having to finagle direct references back and forth between them

    ######################################################
    # Initialization of player and dealer instance variables
    # This section moved to player.py and dealer.py
    # TODO: Delete when you are satisfied with the changes
    ######################################################
    #playerFunds = 100  # just in case we include currency for betting
    # playerCard1, playerCard2, playerHits = 0, 0, 0
    # dealer.card1, dealer.card2, dealerHits = 0, 0, 0
    # set max cards for player declare variables

    # dealCount = 0
    #
    # while dealCount < 10:
    #     dealCount = dealCount + 1
    #     print(random.randint(0, 12))  # okay, so random.randint range apparently includes "0" and "12" in this case




    print("Welcome to Basic Blackjack!")

    #ST: Commented some of these inputs out for quicker testing; I don't know a cleverer way to "wait" as of yet
    #input("Press Enter to continue...") 

    ######################################################
    # Setting up the player's info
    # Yet to be implemented
    # TODO: Implement when desired. Move to player.py
    ######################################################
    # playerName = input("What is your name? ")

    # This next section is currently bonus to try and get betting working
    # print("Hi,", playerName + ".", "You have", "$" + str(playerFunds), "available")
    #
    # playerBet = int(input("How much would you like to wager? "))
    # playerFunds = playerFunds - playerBet
    # I'll work on this more later

    print("Dealing cards...")
    #input("Press Enter to continue...")

    game.player.start()
    ######################################################
    # Player's initial draw and blackjack check
    # This section moved to Player.start() in player.py
    # TODO: Delete when you are satisfied with the changes
    ######################################################
    # player.card1 = random.randint(2, 11)
    # player.card2 = random.randint(1, 10)

    # if player.card1 == 10 and player.card2 == 1:  # Forgot about drawing a "10" then a "1" - this fixes it
    #     player.card2 = 11

    # print("Here are your cards")
    # print("Card 1 =", str(player.card1))
    # print("Card 2 =", str(player.card2))

    # player.total = player.card1 + player.card2 
    # # There's a better way to do this...right?

    # print("Your current total is", str(player.total))
    # if player.total == 21:
    #     print("Blackjack! You win!")
    #     sys.exit()
    # input("Press Enter to continue...")

    game.dealer.start()
    ######################################################
    # Dealer's initial draw and blackjack check
    # This section moved to Dealer.start() in dealer.py
    # TODO: Delete when you are satisfied with the changes
    ######################################################
    # dealer.card1 = random.randint(2,11)
    # dealer.card2 = random.randint(1,10)

    # if dealer.card1 == 10 and dealer.card2 == 1:
    #     dealer.card2 = 11

    # dealer.total = dealer.card1 + dealer.card2

    # if dealer.total == 21:
    #     print("Dealer Blackjack! You lose!")
    #     sys.exit()

    print("The dealer's face-up card is a", str(game.dealer.card2))

    game.player.play()
    ######################################################
    # Player's gameplay section
    # This section moved to Player.play() in player.py
    # TODO: Delete when you are satisfied with the changes
    ######################################################

    # while True:
    #     hitStand = str(input("Hit or Stand? "))
    #     if hitStand == "stand":
    #         break
    #     elif hitStand == "Stand":
    #         break
    #     elif hitStand == "hit":
    #         hitCard = random.randint(1,10)
    #         player.total = player.total + hitCard
    #         playerHits = playerHits + 1
    #         print("You drew a", str(hitCard))
    #         print("Your total is", str(player.total))
    #         #input("Press Enter to continue...")
    #         if playerHits >= 3 and player.total < 22:
    #             print("5 cards drawn. You win!")
    #             break
    #         if player.total > 21:
    #             print("Busted!")
    #             sys.exit()
    #     elif hitStand == "Hit":
    #         hitCard = random.randint(1,10)
    #         player.total = player.total + hitCard
    #         playerHits = playerHits + 1
    #         print("You drew a", str(hitCard))
    #         print("Your total is", str(player.total))
    #         #input("Press Enter to continue...")
    #         if playerHits >= 3 and player.total < 22:
    #             print("5 cards drawn. You win!")
    #             break
    #         if player.total > 21:
    #             print("Busted!")
    #             sys.exit()
    #     else:
    #         print("I didn't get that")

    print("Your current total is", str(game.player.total))
    print("The dealer has a", str(game.dealer.card1), "and a", str(game.dealer.card2), "for a total of", str(game.dealer.total))
    #input("Press Enter to continue...")

    game.dealer.play()
    ######################################################
    # Dealer's gameplay section
    # This section moved to Dealer.play() in dealer.py
    # TODO: Delete when you are satisfied with the changes
    ######################################################
    # if dealer.total == player.total: #ST: I think the standard rule is the dealer will hit on a push, if under 17, so move this down?
    #     print("Push (tied).")
    #     sys.exit()
    # elif dealer.total > player.total:
    #     print("Your total is", str(player.total))
    #     print("The dealer has", str(dealer.total))
    #     print("The dealer wins.")
    #     sys.exit()
    # else:
    #     while dealer.total < 17:
    #         input("The dealer hits. (Press Enter to continue...)")
    #         hitCard = random.randint(1,10)
    #         print("The dealer draws a", str(hitCard))
    #         dealer.total = dealer.total + hitCard
    #         print("The dealer now has", str(dealer.total))
    #         #input("Press Enter to continue...")
    #         if dealer.total > 21:
    #             print("Dealer busts. You win!")
    #             sys.exit()

    ######################################################
    # Determining the winner
    # 
    ######################################################
    print("Your total is", str(game.player.total))
    print("The dealer's total is", str(game.dealer.total))
    #input("Press Enter to continue...")

    # These sys.exit() calls are not needed because only one part of the if/elif/else will execute in any case, and we are at the end of the program anyway. Cutting them allows us to remove the 'import sys' dependency
    if game.dealer.total == game.player.total:
        print("Push (tied).")
        # sys.exit()
    elif game.dealer.total > game.player.total:
        print("The dealer wins.")
        # sys.exit()
    else:
        print("You win!")
        # sys.exit()

main()
