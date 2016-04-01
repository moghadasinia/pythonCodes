# Black Jack game
import simplegui
import random 

#globals
RANKS = ('A','2','3','4','5','6','7','8','9','T','J','Q','K')
SUITS = ('C','S','H','D')
VALUES = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':10,'Q':10,'K':10}
WIDTH = 5*73
HEIGHT = 200

#card sprites
CARD_CENTER = (36.5,49)
CARD_SIZE = (73,98)
image = simplegui.load_image("https://www.dropbox.com/s/26eijiv4kauliaj/cards.png?dl=1")
qty = 5

# Classes
#define Card Class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank+" of "+self.suit
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
        
    def draw(self,canvas,loc):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)

        card_pos = [CARD_CENTER[0]+ i * CARD_SIZE[0],CARD_CENTER[1]+ j * CARD_SIZE[1]]
        canvas.draw_image(image,card_pos,CARD_SIZE,loc,CARD_SIZE)

#define Hand Class
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.has_ace = False
       # self.ace_qty = 0
    def __str__(self):
        return str(self.cards)
    
    def add_card(self,card):
        self.cards.append(card)
        if card.rank == 'A':
            self.has_ace = True
        self.value += VALUES[card.rank]
            
    #count Aces as 1, if the hand has an Ace,then add 10...
    def get_value(self):
        if self.has_ace == True:
            if self.value + 10 < 21:
                #return self.value + 10
                self.value += 10
            #else:
             #   return self.value
        return self.value
    
    def busted(self):
        if self.value > 21:
            return True
        else:
            return False
    
    def draw(self,canvas,p):
        for i in range(len(self.cards)):
            x = p[0]+i*CARD_CENTER[0]
            y = p[1]
            q =(x,y)
            self.cards[i].draw(canvas,q)
    
#define Deck Class       
class Deck:
    def __init__(self):
        pass
    
    #add cards back to deck and shuffle
    def shuffle(self):
        pass
    
    def deal_card(self):
        pass
        
#draw handler
def draw(canvas):
    myhand.draw(canvas,(100,90))
 
#set frame
frame = simplegui.create_frame("Black Jack", WIDTH,HEIGHT)
frame.set_draw_handler(draw)

#Create Cards and add to hand
myhand = Hand()
while myhand.value <17:
    myhand.add_card(Card(random.choice(SUITS),random.choice(RANKS)))

#mycard = Card('S','A')
#myhand.add_card(mycard)

print myhand.value
print myhand.get_value()
print myhand.value
print "has Ace : "+str(myhand.has_ace)
print "busted : "+str(myhand.busted())

frame.start()
