# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:30:32 2019

@author: Logan Price, Billy Pilkin, and Petter Johansen
"""

import random, copy, yahtzee_gui as gui
import os
import psutil



class Game(object):
    def __init__(self, gamemode=None, players=0, player_names=list(), locked_Dice=[0,0,0,0,0]):
        self.gamemode = gamemode
        self.players = players
        self.player_names = player_names
        self.locked_Dice = locked_Dice
        self.die1, self.die2, self.die3, self.die4, self.die5, = Die(), Die(), Die(), Die(), Die() 
        self.scoreboard = Scoreboard(self)
        self.current_player = Player("temp")
        self.show_buttons = False
        self.roll_number = 1
        self.round = 0
        self.display = False
    
    def set_gamemode(self, gamemode):
        self.gamemode = gamemode
        #print("gamemode is now", self.gamemode)
        
    def set_players(self, players):
        self.players = players
        #print("There are", self.players, "players")
    
    def set_player_names(self, player_name_list):
        self.player_names= []
        for player in player_name_list:
            self.player_names.append(Player(player))
        self.current_player = self.player_names[0]
        
        #print("player names are now {}".format(', '.join([str(x) for x in self.player_names])))
        #print("current player is:", self.current_player)
        
    def get_players(self):
        return self.players
    
    def check_memory(self):
        '''used to check for memory leaks'''
        process = psutil.Process(os.getpid())
        print("Memory: {}".format(process.memory_info().rss))
        
    def get_player_names(self):
        return self.player_names
    
    def get_gamemode(self):
        return self.gamemode
    
    def get_roll_number(self):
        return self.roll_number
    
    def set_roll_number(self):
        self.roll_number = 1
        
    def set_Locked_Dice(self,index, status):
        if status == "Locked":
            self.locked_Dice[index] = 1
        if status == "Hold":
            self.locked_Dice[index] = 0
        #print(self.locked_Dice)
    
    def roll_dice(self):
        '''rolls all 5 die instances'''
        self.die1.roll()
        self.die2.roll()
        self.die3.roll()
        self.die4.roll()
        self.die5.roll()
        #print(self.die1, self.die2, self.die3, self.die4, self.die5)
        
    def next_player(self):
        '''changes to the next players turn'''
        play_num = 10 #this is a number out of range of possible players
        for i,p in enumerate(self.player_names):
            if self.current_player == p:
                play_num = i
                break
            
        if play_num+1 < len(self.player_names):       
            self.current_player = self.player_names[play_num+1]
        else:
            self.current_player = self.player_names[0]
        #print("current player is now:", self.current_player)
        
    def show_buttons_flip(self):
        self.show_buttons = False
        #print("Buttons on:", self.show_buttons)
    
    def show_buttons_true(self):
        self.show_buttons = True
        #print("Buttons are now off")
        
    def update_roll_number(self):
        if self.roll_number < 3:
            self.roll_number += 1
            
    def unlock_dice(self):
        self.die1.unlock()
        self.die2.unlock()
        self.die3.unlock()
        self.die4.unlock()
        self.die5.unlock()
    
    def set_round(self):
        '''method that skips scores that aren't rolled for i.e. total, bonus, etc.'''
        length = len(self.player_names)
        if self.current_player == self.player_names[length - 1]:
            self.round += 1
        if self.round == 6:
            self.round = 9
        if self.round == 18:
            self.round = 0
    
    def get_round(self):
        return self.round
    
    def set_display(self):
        if self.display == False:
            self.display = True
        else:
            self.display = False

    def rematch(self):
        '''resets stats for a rematch'''
        self.round = 0
        self.roll_number = 1
        player_names = self.player_names
        self.player_names= []
        for player in player_names:
            self.player_names.append(Player(player.name))
        self.current_player = self.player_names[0]
        self.set_display()
        
    def reset(self):
        self.round = 0
        self.set_display()
        self.roll_number = 1
            
        
class Player(object):
    def __init__(self, name):
        self.name = name[:15] #makes the max length 15 characters
        self.scores = \
        {"Ones": -1,
         "Twos": -1,
         "Threes": -1,
         "Fours": -1,
         "Fives": -1,
         "Sixes": -1,
         "Total": -1,
         "Bonus": -1,
         "Upper Total": -1,
         "One Pair": -1,
         "Two Pairs": -1,
         "3 of a Kind": -1,
         "4 of a Kind": -1,
         "Small Straight": -1,
         "Large Straight": -1,
         "Full House": -1,
         "YAHTZEE": -1,
         "Chance": -1,
         "Lower Total": -1,
         "Grand Total": -1}
    
    def __str__(self):
        return self.name
        
    def add_score(self, category, score):
        self.scores[category] = score
    
    def get_scores(self):
        return copy.deepcopy(self.scores)

        
class Die(object):
    def __init__(self):
        self.locked = False
        self.value = random.randint(1,6)
        
    def get_locked(self):
        return self.locked
    
    def get_value(self):
        return self.value
    
    def toggle_lock(self):
        self.locked = not self.locked
    
    def unlock(self):
        self.locked = False
    
    def roll(self):
        if not self.locked:
            self.value = random.randint(1,6)
    
    def __str__(self):
        return str(self.value)

class Scoreboard(object):
    def __init__(self, controller):
        self.controller = controller
    
    def calculate_score(self, category, dice):
        '''returns the score based on the category'''
        total = 0
        sort_dice = sorted(dice)
        
        if category == "Ones":
            for i in range(5):
                if dice[i] == 1:
                    total += 1
            return total
        elif category == "Twos":
            for i in range(5):
                if dice[i] == 2:
                    total += 2
            return total
        elif category == "Threes":
            for i in range(5):
                if dice[i] == 3:
                    total += 3
            return total
        elif category == "Fours":
            for i in range(5):
                if dice[i] == 4:
                    total += 4
            return total
        elif category == "Fives":
            for i in range(5):
                if dice[i] == 5:
                    total += 5
            return total
        
        elif category == "Sixes":
            for i in range(5):
                if dice[i] == 6:
                    total += 6
            return total
        
        elif category == "One Pair":
            if sort_dice[-1] == sort_dice[-2]:
                total = sort_dice[-1] + sort_dice[-2]
            elif sort_dice[-2] == sort_dice[-3]:
                total = sort_dice[-2] + sort_dice[-3]    
            elif sort_dice[-3] == sort_dice[-4]:
                total = sort_dice[-3] + sort_dice[-4]
            elif sort_dice[-4] == sort_dice[-5]:
                total = sort_dice[-4] + sort_dice[-5]              
            return total
        
        elif category == "Two Pairs":
            if sort_dice[0] == sort_dice[1] and sort_dice[2] == sort_dice[3]:
                if sort_dice[1] != sort_dice[2]:
                    total = sort_dice[0] + sort_dice[1] + sort_dice[2] + sort_dice[3]
            elif sort_dice[0] == sort_dice[1] and sort_dice[3] == sort_dice[4]:
                if sort_dice[1] != sort_dice[3]:
                    total = sort_dice[0] + sort_dice[1] + sort_dice[3] + sort_dice[4]    
            elif sort_dice[1] == sort_dice[2] and sort_dice[3] == sort_dice[4]:
                if sort_dice[2] != sort_dice[3]:
                    total = sort_dice[1] + sort_dice[2] + sort_dice[3] + sort_dice[4]
                    
            return total
          
        elif category == "3 of a Kind":
            if sort_dice[0] == sort_dice[1] and sort_dice[1] == sort_dice[2]:
                total = sort_dice[0] + sort_dice[1] + sort_dice[2]
            elif sort_dice[1] == sort_dice[2] and sort_dice[2] == sort_dice[3]:
                total = sort_dice[1] + sort_dice[2] + sort_dice[3]    
            elif sort_dice[2] == sort_dice[3] and sort_dice[3] == sort_dice[4]:
                total = sort_dice[2] + sort_dice[3] + sort_dice[4]
            return total
        
        elif category == "4 of a Kind":
            if sort_dice[0] == sort_dice[1] and sort_dice[1] == sort_dice[2] and sort_dice[2] == sort_dice[3]:
                total = sort_dice[0] + sort_dice[1] + sort_dice[2] + sort_dice[3]
            elif sort_dice[1] == sort_dice[2] and sort_dice[2] == sort_dice[3] and sort_dice[3] == sort_dice[4]:
                total = sort_dice[1] + sort_dice[2] + sort_dice[3] + sort_dice[4]
            return total
        
        elif category == "Full House":
            if sort_dice[0] == sort_dice[1] and sort_dice[0] == sort_dice[2] and sort_dice[3] == sort_dice[4]:
                total = 25
            elif sort_dice[0] == sort_dice[1] and sort_dice[2] == sort_dice[3] and sort_dice[2] == sort_dice[4]:
                total = 25
            return total
        
        elif category == "Small Straight":
            if 1 in set(sort_dice) and 2 in set(sort_dice) and 3 in set(sort_dice) and 4 in set(sort_dice) or \
            2 in set(sort_dice) and 3 in set(sort_dice) and 4 in set(sort_dice) and 5 in set(sort_dice) or \
            3 in set(sort_dice) and 4 in set(sort_dice) and 5 in set(sort_dice) and 6 in set(sort_dice):
                total = 30
            return total
        
        elif category == "Large Straight":
            if sort_dice == [1,2,3,4,5] or sort_dice == [2,3,4,5,6]:
                total = 40
            return total
        
        elif category == "YAHTZEE":
            if len(set(dice)) == 1:
                total = 50
            return total
        
        elif category == "Chance":
            for i in range(5):
                total += dice[i]
            return total
    
    def set_score (self, category):
        '''method that sets the score after calculating it'''
        player = self.controller.current_player
        
        
        dice = [self.controller.die1.get_value(), self.controller.die2.get_value(), self.controller.die3.get_value(), self.controller.die4.get_value(), self.controller.die5.get_value()]
        score = self.calculate_score(category, dice)
        player.add_score(category, score)
        
        scores = player.get_scores()
        
        for key in scores: # this is done to not calculate the -1's
            if scores[key] == -1:
                scores[key] = 0
        
        player.add_score("Total", scores["Ones"]+scores["Twos"]+scores["Threes"]+scores["Fours"]+scores["Fives"]+scores["Sixes"])
        player.add_score("Bonus", 35 if player.get_scores()["Total"] >= 63 else 0)
        player.add_score("Upper Total", player.get_scores()["Total"]+player.get_scores()["Bonus"])
        player.add_score("Lower Total", scores["One Pair"]+scores["Two Pairs"]+scores["3 of a Kind"]+scores["4 of a Kind"]+scores["Small Straight"]+scores["Large Straight"]+scores["Full House"]+scores["YAHTZEE"]+scores["Chance"])
        player.add_score("Grand Total", player.get_scores()["Upper Total"]+player.get_scores()["Lower Total"])
        
    def calculate_winner (self):
        winner = ["", 0]
        total = 0
        players = self.controller.player_names
        for player in players:
            grand_total = player.get_scores()["Grand Total"]
            if grand_total > total:
                winner[0] = str(player)
                winner[1] = grand_total
                total = grand_total

        return winner
       
        
game1 = Game()    
root = gui.App(game1)
root.mainloop()
