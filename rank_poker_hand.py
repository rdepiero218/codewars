#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:40:45 2024

@author: reggiemba
"""
import re

class PokerHand(object):
    
    def __init__(self, hand):
        
        card_val = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,'A': 14}
        self.hand = hand
        self.cards = self.hand.split(' ')
        
        #find suits
        self.suits = re.findall(r'[HSCD]', hand)
        
        #find vals
        vals = re.findall(r'[2-9TJQKA]', hand)
        self.vals = [card_val[val] for val in vals]
        
        self.is_consecutive = self.consecutive()
        self.is_same_suit = self.same_suit()
        self.card_sets = self.find_sets()
        self.hand_type = self.classify_hand()
        
        # self.high_card = [i for i in card_val if card_val[i]== max(self.vals)][0]
        
        pass
    
    def consecutive(self):
        # need case for A as low card in flush
        
        
        if sorted(self.vals) == list(range(min(self.vals), max(self.vals)+1)) or (sorted(self.vals) == [2,3,4,5,14]):
            return True
        else:
            return False
        
    def same_suit(self):
        if len(set(self.suits)) == 1:
            return True
        else:
            return False
        
    def high_card(self, card_list):
        
        # high_card = [i for i in card_list if card_listl[i] == max(card_list)][0]
        high_card = max(card_list)
        
        return high_card
        
    def straight_or_flush(self):
        if sorted(self.vals) == list(range(10,15)) and self.same_suit():
            return 'Royal Flush'
        
        elif self.consecutive() and self.same_suit():
            return 'Straight Flush'
        
        elif self.consecutive() and not self.same_suit():
            return 'Straight'
        
        elif not self.consecutive() and self.same_suit():
            return 'Flush'
        else:
            return False
        
    def find_sets(self):
        duplicates = [val for val in self.vals if self.vals.count(val) > 1]
        duplicates.sort()
        duplicate_set = set(duplicates)
        
        card_sets = [[s for val in range(duplicates.count(s)) ] for s in duplicate_set]
        
        # if length card_sets >1, then find length of each list
        # then you can easily test value of cards in each set as needed.
    
        return card_sets  
    
    def classify_hand(self):
        
        if self.straight_or_flush():
            hand_type = self.straight_or_flush()
            
        elif self.classify_sets():
            hand_type = self.classify_sets()
        else:
            hand_type = 'Nothing'
        
        return hand_type
        
        
    # def find_sets(self):
    #     duplicates = [val for val in self.vals if self.vals.count(val) > 1]
    #     num_cards = len(duplicates)
    #     duplicates.sort()
        
    #     # card_sets = list(set(duplicates))
    #     # print('Num dups: ', dup_length)
    #     num_sets = len(set(duplicates))
    #     # print('unique dups: ', count_duplicates)
    #     return num_cards, duplicates, num_sets
    def classify_sets(self):
         
        # find length of each card set
        set_lengths = [len(card_set) for card_set in self.card_sets]
        
        if not self.card_sets:
            return False
        elif len(self.card_sets) == 2:
            if 3 in set_lengths:
                return 'Full House'
            else:
                return '2 Pair'
        elif set_lengths[0] == 4:
            return '4 of a Kind'
        elif set_lengths[0] == 3:
            return '3 of a Kind'
        
        elif set_lengths[0] == 2 and self.card_sets[2] == 1:
            return '1 Pair'  
    
    # def kinds(self):
        
    #     card_sets = self.find_sets()
        
    #     # find length of each card set
    #     set_lengths = [len(card_set) for card_set in card_sets]
        
    #     if len(card_sets) == 2 and (3 in set_lengths):
    #         return 'Full House'
            
    #     if card_sets[0] == 5 and card_sets[2] == 2:
    #         return 'Full House'
    #     elif card_sets[0] == 4 and card_sets[2] == 1:
    #         return '4 of a Kind'
    #     elif card_sets[0] == 3 and card_sets[2] == 1:
    #         return '3 of a Kind'
    #     elif card_sets[0] == 4 and card_sets[2] == 2:
    #         return '2 Pair'
    #     elif card_sets[0] == 2 and card_sets[2] == 1:
    #         return '1 Pair'
    #     else:
    #         return False
        
    def compare_with(self, other):
        RESULT = ["Loss", "Tie", "Win"]
        rank = ['Nothing', 'Pair', 'Two Pair', '3 of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']
        
        player_hand = self.hand_type
        opp_hand = other.hand_type
        
        player_hand_rank = rank.index(player_hand)
        opp_hand_rank = rank.index(opp_hand)
        
        if player_hand_rank > opp_hand_rank:
            return RESULT[2]
        
        elif player_hand_rank < opp_hand_rank:
            return RESULT[0]
        
        elif player_hand_rank == opp_hand_rank:
            
            return RESULT[1]
    
    
    
# vals_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
   # 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A 
rank = [
        'Royal Flush',
        'Straight Flush',
        'Four of a Kind',
        'Full House',
        'Flush',
        'Straight',
        '3 of a Kind',
        'Two Pair',
        'Pair'
        ]   
# hand = "2H 3H 4H 5H 6H"
# hand = 'KS AS TS QS JS'
# hand = '2S 3H 4H 5S 6C' # straight
hand = 'AS 3H 4H 2S 5C' # straight A low
# hand = 'AH AC 5H 6H AS' # 3 kind
# hand = '2S 2H 4H 5S 4C' # 2 pair
# hand = '2S AH 2H AS AC' # full house
# hand = 'JS JD JC JH AD' # 4 of a kind
# hand = 'AH AC 5H 6H 7S' # Pair
other =  "KS AS TS QS JS"
player, opponent = PokerHand(hand), PokerHand(other)

print('Cards: ', player.hand)
print('consecutive:', player.is_consecutive)
print('same suit:', player.is_same_suit)
print('straight/Flush: ', player.straight_or_flush())
print('card sets: ', player.find_sets())
print('Classify Pairs: ', player.classify_sets())
print('PLAYER Hand: ', player.classify_hand())
print('OPPONENT Hand: ', opponent.classify_hand())

# print('high card: ', player.high_card)

print('Result:', player.compare_with(opponent))

# runTest("Highest straight flush wins",        "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
# runTest("Straight flush wins of 4 of a kind", "Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")
# runTest("Highest 4 of a kind wins",           "Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")
# runTest("4 Of a kind wins of full house",     "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
# runTest("Full house wins of flush",           "Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
# runTest("Highest flush wins",                 "Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")
# runTest("Flush wins of straight",             "Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")
# runTest("Equal straight is tie", 	  	      "Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")
# runTest("Straight wins of three of a kind",   "Win",  "2S 3H 4H 5S 6C", "AH AC 5H 6H AS")
# runTest("3 Of a kind wins of two pair",       "Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")
# runTest("2 Pair wins of pair",                "Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")
# runTest("Highest pair wins",                  "Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")
# runTest("Pair wins of nothing",               "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
# runTest("Highest card loses",                 "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
# runTest("Highest card wins",                  "Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")
# runTest("Equal cards is tie",		          "Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")