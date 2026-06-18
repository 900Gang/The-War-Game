suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
import random

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank=rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                creat_card = Card(suit,rank)
                self.all_cards.append(creat_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_cards(self,cards):
        pass


    def adjust_for_ace(self):
        pass


class chips:
    def __init__(self):
        self.total = 100
        self.bet=0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass

def take_bet():
    pass

def hit(deck,hand):
    pass

def hit_or_stand(deck,hand):
    global playing
    pass

def show_some(player,dealer):
    pass

def show_all(player,dealer):
    pass
def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass

def dealer_win():
    pass

def push():
    pass

playing = True


while True:




    while playing:







        break

        

            
   
















