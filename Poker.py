# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:53:44 2018

@author: suraj
"""

#Generating Pascal traingle for practice
lst = [1]

for i in range(10):
    print(lst)
    newlst = [lst[0]]
    for i in range(len(lst)-1):
        newlst.append(lst[i]+lst[i+1])
    newlst.append(lst[-1])
    lst = list(newlst)

#Let's play Poker
###### Poker - Cards
suits = ['\u2660','\u2665','\u2666','\u2663']   #unicodes for suits
cards = ['A','2','3','4','5','6','7','8','9',\
         '10','J','Q','K']

#creating a deck
deck = []
for suit in suits:
    for card in cards:
        deck.append(card+suit)
print(deck)

#Shuffling the cards
import random
random.seed(52)

rando = [random.random() for i in range(52)]
#for i in enumerate(rando): print (i)
rando = [i[0] for i in sorted(enumerate(rando), key=lambda x:x[1])]
shuffle = [deck[x] for x in rando]
print(shuffle)

#poker hand
hand = shuffle[0:5]
