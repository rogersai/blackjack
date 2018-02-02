import random
import sys

playerFunds = 100  # just in case we include currency for betting
playerCard1, playerCard2, playerHits = 0, 0, 0
dealerCard1, dealerCard2, dealerHits = 0, 0, 0
# set max cards for player declare variables

# dealCount = 0
#
# while dealCount < 10:
#     dealCount = dealCount + 1
#     print(random.randint(0, 12))  # okay, so random.randint range apparently includes "0" and "12" in this case

print("Welcome to Basic Blackjack!")
input("Press Enter to continue...")

# playerName = input("What is your name? ")

# This next section is currently bonus to try and get betting working
# print("Hi,", playerName + ".", "You have", "$" + str(playerFunds), "available")
#
# playerBet = int(input("How much would you like to wager? "))
# playerFunds = playerFunds - playerBet
# I'll work on this more later

print("Dealing cards...")
input("Press Enter to continue...")
playerCard1 = random.randint(2, 11)
playerCard2 = random.randint(1, 10)

if playerCard1 == 10 and playerCard2 == 1:  # Forgot about drawing a "10" then a "1" - this fixes it
    playerCard2 = 11

print("Here are your cards")
print("Card 1 =", str(playerCard1))
print("Card 2 =", str(playerCard2))

playerTotal = playerCard1 + playerCard2
# There's a better way to do this...right?

print("Your current total is", str(playerTotal))
if playerTotal == 21:
    print("Blackjack! You win!")
    sys.exit()
input("Press Enter to continue...")

dealerCard1 = random.randint(2,11)
dealerCard2 = random.randint(1,10)

if dealerCard1 == 10 and dealerCard2 == 1:
    dealerCard2 = 11

dealerTotal = dealerCard1 + dealerCard2

if dealerTotal == 21:
    print("Dealer Blackjack! You lose!")
    sys.exit()

print("The dealer's face-up card is a", str(dealerCard2))

while True:
    hitStand = str(input("Hit or Stand? "))
    if hitStand == "stand":
        break
    elif hitStand == "Stand":
        break
    elif hitStand == "hit":
        hitCard = random.randint(1,10)
        playerTotal = playerTotal + hitCard
        playerHits = playerHits + 1
        print("You drew a", str(hitCard))
        print("Your total is", str(playerTotal))
        input("Press Enter to continue...")
        if playerHits >= 3 and playerTotal < 22:
            print("5 cards drawn. You win!")
            break
        if playerTotal > 21:
            print("Busted!")
            sys.exit()
    elif hitStand == "Hit":
        hitCard = random.randint(1,10)
        playerTotal = playerTotal + hitCard
        playerHits = playerHits + 1
        print("You drew a", str(hitCard))
        print("Your total is", str(playerTotal))
        input("Press Enter to continue...")
        if playerHits >= 3 and playerTotal < 22:
            print("5 cards drawn. You win!")
            break
        if playerTotal > 21:
            print("Busted!")
            sys.exit()
    else:
        print("I didn't get that")

print("Your current total is", str(playerTotal))
print("The dealer has a", str(dealerCard1), "and a", str(dealerCard2), "for a total of", str(dealerTotal))
input("Press Enter to continue...")

if dealerTotal == playerTotal:
    print("Push (tied).")
    sys.exit()
elif dealerTotal > playerTotal:
    print("Your total is", str(playerTotal))
    print("The dealer has", str(dealerTotal))
    print("The dealer wins.")
    sys.exit()
else:
    while dealerTotal < 17:
        input("The dealer hits. (Press Enter to continue...)")
        hitCard = random.randint(1,10)
        print("The dealer draws a", str(hitCard))
        dealerTotal = dealerTotal + hitCard
        print("The dealer now has", str(dealerTotal))
        input("Press Enter to continue...")
        if dealerTotal > 21:
            print("Dealer busts. You win!")
            sys.exit()

print("Your total is", str(playerTotal))
print("The dealer's total is", str(dealerTotal))
input("Press Enter to continue...")

if dealerTotal == playerTotal:
    print("Push (tied).")
    sys.exit()
elif dealerTotal > playerTotal:
    print("The dealer wins.")
    sys.exit()
else:
    print("You win!")
    sys.exit()
