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
    


    def __str__(self):
        deck_com=''
        for card in self.all_cards:
            deck_comp+='\n'+ card.__str__()
        return "The deck has: "+deck_com



    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        single_card=self.all_cards.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank=='Ace':
            self.aces+=1


    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value-=10
            self.aces-=1
        


class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet=0

    def win_bet(self):
        self.total+= self.bet

    def lose_bet(self):
        self.total-=self.bet

def take_bet():
    while True:
        chip=Chips()
        try:
            chip.bet=int(input("Enter the bet amount you want to give:"))
        except:
            print("Only Integer Values !!!!!")
        else:
            if chip.bet>chip.total:
                print("You don't have enough chips available with you, {} is your balance amount".format(chip.total))
            else: 
                break


    

def hit(deck,hand):
    deck=Deck()
    hand=Hand()
    Single_card=deck.deal_one()
    hand.add_cards(Single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x =input("Hit or Stand ? Enter 'h' or 's'").split(" ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stand's Dealer's Turn")
            playing=False
        else:
            print("Sorry , I did not understand that , Please enter 'h' or 's' ")
            continue
        break



def show_some(player,dealer):
    print("\n Dealer's Hand: ")
    print("First Card Hidden! ")
    print(dealer.cards[1])

    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)



def show_all(player,dealer):
    print("\n Dealer's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Dealer's hand is : {dealer.value}")



    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is : {dealer.value}")



def player_busts(player,dealer,chips):
    chip=Chips()
    print("BUST PLAYER !")
    chip.lose_bet()
    

def player_wins(player,dealer,chips):
    chip=Chips()
    print("PLAYER WINS!")
    chip.win_bet()

def dealer_busts(player,dealer,chips):
    chip=Chips()
    print("PLAYER WINS! DEALER BUSTED!")
    chip.win_bet()

def dealer_win(player,dealer,chips):
    chip=Chips()
    print("DEALER WINS !")
    chip.lose_bet()

def push(player,dealer,chips):
    print("Dealer and player tie! PUSH")

playing = True


while True:
    print("WELCOME TO CASINO $$$$$$$")
    
    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_cards(deck.deal_one())
    player_hand.add_cards(deck.deal_one())

    dealer_hand=Hand()
    dealer_hand.add_cards(deck.deal_one())
    dealer_hand.add_cards(deck.deal_one())


    player_chips=Chips()

    take_bet(player_chips)


    show_some(player_hand,dealer_hand)

    


    while playing:

        hit_or_stand( deck,player_hand)

        show_some(player_hand,dealer_hand)


        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break


        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_win(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)


        print('\n Player total chips are at : {} '.format(player_chips.total))

        newgame=input("Would you like to play another hand? y/n")

        if newgame[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thank You For Playing!")

            break

        

            
   
















