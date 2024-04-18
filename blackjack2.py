import random

class Deck:
    
    def __init__(self):
        self.deck=[
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
    
    def shuffle(self):
        return random.shuffle(self.deck)
    
    def draw(self):
        return self.deck.pop(0) 
    
    def __str__(self):
        return ', '.join(self.deck)
        
    
        
        
deck = Deck()
# print(f"Before: {deck}")
deck.shuffle()
print(deck)
print(deck.draw())



