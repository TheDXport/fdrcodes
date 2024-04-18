import random

class Deck():
    def __init__(self):
        self.deck = [
    "♣3", "♦3", "♥3", "♠3",
    "♣4", "♦4", "♥4", "♠4",
    "♣5", "♦5", "♥5", "♠5",
    "♣6", "♦6", "♥6", "♠6",
    "♣7", "♦7", "♥7", "♠7",
    "♣8", "♦8", "♥8", "♠8",
    "♣9", "♦9", "♥9", "♠9",
    "♣10","♦10", "♥10", "♠10",
    "♣J", "♦J", "♥J", "♠J",
    "♣Q", "♦Q", "♥Q", "♠Q",
    "♣K", "♦K", "♥K", "♠K",
    "♣A", "♦A", "♥A", "♠A",
    "♣2", "♦2", "♥2", "♠2",
]
    
    def revealCard(self):
        return self.deck.pop(0)
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    
    
def convertCourtCardstoNums(card, currentPoints):
    toBeAddedPoints = 0
    if card[1:] == "J" or card[1:] == "Q" or card[1:] == "K":
        toBeAddedPoints += 10 
    elif card[1:] == "A":
        if currentPoints + 11 < 22:
            toBeAddedPoints += 11
        else:
            toBeAddedPoints += 1
    else:
        toBeAddedPoints += int(card[1:])
    return toBeAddedPoints


    


deck = Deck()
deck.shuffle()
print(deck)

userCards = []
userCards.append(deck.revealCard())
userCards.append(deck.revealCard())

dealerCards = []
dealerCards.append(deck.revealCard())   
dealerCards.append(deck.revealCard())   
   
print()

userPoints = 0
dealerPoints = 0 

def showGameStats():
    print(f"Your cards:")
    for card in userCards:
        print(f"{card}")
    print(f"Your points: {userPoints}")
    print()   
    print(f"Dealer cards:")
    for card in dealerCards: 
        print(f"{card}")
    print(f"Dealer's points: {dealerPoints}")
    
    
    
for card in userCards:
    userPoints += convertCourtCardstoNums(card, userPoints)

for card in dealerCards:
    dealerPoints += convertCourtCardstoNums(card, dealerPoints)

showGameStats()
    
# Hit or Stand?
if userPoints == 21 or dealerPoints > 21:
    print("You won!")
elif dealerPoints == 21:
    print("Dealer won!")
elif userPoints > 21:
    print("Bust!")
else:   
    userInput = input("(H)it or (S)tand?\n")
    if userInput == "H":
        newUserCard = deck.revealCard()
        userCards.append(newUserCard)
        userPoints += convertCourtCardstoNums(newUserCard, userPoints)
        if dealerPoints < 18:
            newDealerCard = deck.revealCard()
            dealerCards.append(newDealerCard)
            dealerPoints += convertCourtCardstoNums(newDealerCard, dealerPoints)
            
        
            
        if userPoints == 21 or dealerPoints > 21:
            print("You won!")
            showGameStats()
            exit()
        elif dealerPoints == 21:
            print("Dealer won!")
            showGameStats()
            exit()
        elif userPoints > 21:
            print("Bust!")
            showGameStats()
            exit()
        else:   
            showGameStats()
            userInput = input("(H)it or (S)tand? ")
            if userInput == "H":
                newUserCard = deck.revealCard()
                userCards.append(newUserCard)
                userPoints += convertCourtCardstoNums(newUserCard, userPoints)
                if dealerPoints < 18:
                    newDealerCard = deck.revealCard()
                    dealerCards.append(newDealerCard)
                    dealerPoints += convertCourtCardstoNums(newDealerCard, dealerPoints)
            elif userInput == "S":
                newDealerCard = deck.revealCard()
                if dealerPoints < 18:
                    dealerCards.append(newDealerCard)
                    dealerPoints += convertCourtCardstoNums(newDealerCard, dealerPoints)



        
            
            
    elif userInput == "S":
        newDealerCard = deck.revealCard()
        if dealerPoints < 18:
            dealerCards.append(newDealerCard)
            dealerPoints += convertCourtCardstoNums(newDealerCard, dealerPoints)
                
        
        


    
if userPoints == 21 or dealerPoints > 21:
    print("You won!")
    showGameStats()
elif dealerPoints == 21:
    print("Dealer won!")
    showGameStats()
elif userPoints > 21:
    print("Bust!")
    showGameStats()
else:
    if abs(21 - userPoints) < abs(21 - dealerPoints):
        print("You won!")
        showGameStats()
    elif abs(21 - userPoints) > abs(21 - dealerPoints):
        print("You lost!")
        showGameStats()

    else: 
        print("No winner!")
        showGameStats()


# if userCard1[1] == "J" or userCard1[1] == "Q" or userCard1[1] == "K":
#     currentPoints += 10
# else:
#     currentPoints += int(userCard1[1:])
    
# if userCard2[1] == "J" or userCard2[1] == "Q" or userCard2[1] == "K":
#     currentPoints += 10
# else:
#     currentPoints += int(userCard2[1:])
    
# print(currentPoints)





# if currentPoints > 21:
#     print("BUST!!!")

# if dealerPoints > 21: 
#     print("YOU WON!!!")

# userChoice = input("(H)it or (S)tand?")
# if userChoice == "H" or userChoice == "h" or userChoice == "hit" or userChoice == "Hit":
#     deck.pop(0)
    

