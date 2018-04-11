# Deck.py

from random import randrange
import random 
from Card import Card
  
class Deck(object):

    #------------------------------------------------------------

    def __init__(self):

        """post: Creates a 52 card deck in standard order"""

        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank,suit))
        self.cards = cards
        self.L = len(self.cards) 

    #------------------------------------------------------------

    def size(self):

        """Cards left
        post: Returns the number of cards in self"""
        
        return self.L # Using instance variable does not change the runnig time of the code
        # becauce python length method has theta constant efficiency and python instance 
        #variables store reference to the data objets.
         
    

    #------------------------------------------------------------

    def deal(self):

        """Deal a single card
        pre:  self.size() > 0
        post: Returns the next card in self, and removes it from self.""" 
        if self.L >0:
            self.L -=1
            return self.cards.pop()
        return False

    #------------------------------------------------------------

    def shuffle(self):

        """Shuffles the deck
        post: randomizes the order of cards in self"""
        random.shuffle(self.cards)

    #-------------------------------------------------------------
    def addTop(self,card):
        
        """adds card back on the top of the deck
        post: put the card back on the top of the deck """
        if self.L >= 0:
            self.insert(0,card)
        self.L += 1



    #-------------------------------------------------------------
    def addBottom(self):
        """adds card back at the bottom of the deck 
        post: put the card back on the bottom of the deck """
        if self.L >= 0:
            self.insert(self.L,card)
        self.L += 1



    #--------------------------------------------------------------
    def addRandom(self,card):
        """adds card back on random place of the deck 
        post: put the card back on random place of the deck """
        if self.L >= 0:
            pos = randrange(0,self.L)
            self.insert(pos,card)
        self.L += 1
        

