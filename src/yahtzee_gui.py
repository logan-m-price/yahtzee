# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:23:38 2019

@author: Logan Price, Billy Pilkin, and Petter Johansen
"""
import tkinter as tk

class App(tk.Tk):
    def __init__(self, game):
        tk.Tk.__init__(self)
        self.game = game
        self.geometry("1000x1000")
        self.resizable(0, 0)
        self.container = tk.Frame(self)
        self.container.pack_propagate(0)
        self.container.pack(fill = tk.BOTH, expand = 1)
        self.container.pack()
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)            
        
        self.make_frame(MainMenu)
        self.show_frame(MainMenu)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def make_frame(self, what_frame):
        '''this method makes each of the screens (frames)'''
        self.frames = {}
        PAGES = (MainMenu, GameModeGui, GameScreenGui, DisplayWinnerGui, NumPlayersGui, NameOfPlayersGui, DisplayScoreboardGui)
        
        for f in PAGES:
            if what_frame == f:
                frame = f(self.container, self)
                frame.configure(bg = "black")
                self.frames[f] = frame
                frame.grid(row=0, column=0, sticky="nsew")

           

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = tk.PhotoImage(file="Yahtzee-logo-600x257.gif")
        logoHeader = tk.Label(self, image=img, bg="black")
        logoHeader.image = img
        logoHeader.pack(pady=20, padx=20)
        
        img = tk.PhotoImage(file="pair of dice.gif")
        dicePicture = tk.Label(self, image=img, bg="black")
        dicePicture.image = img
        dicePicture.place(x = 275, y = 275)
        
        button1 = tk.Button(self, text="New Game", bg="white", font=(None, 12), command=lambda: [self.remove_frame(), controller.make_frame(GameModeGui), controller.show_frame(GameModeGui)])
        button1.place(x = 400, y = 550)
        
        button2 = tk.Button(self, text="Rules", bg="white", font=(None, 12), command=rules)
        button2.place(x = 550, y = 550)
        
    def remove_frame(self):
        self.destroy()
        #print("Frame Destroyed")
        
class GameModeGui(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #buttons for picking gamemode and fram switching
        modeLabel = tk.Label(self, text="Choose Game Mode",font = "Helvetica 30 bold italic", bg="black", fg="red")
        modeLabel.pack(pady=20, padx=20)
        button1 = tk.Button(self, text="Straight", bg="red", fg="black",font = ("Helveteica 20 bold italic"), height = 2, width = 15, command=lambda:[self.remove_frame(), controller.make_frame(NumPlayersGui), controller.show_frame(NumPlayersGui), controller.game.set_gamemode(0)])
        button1.place(x = 350, y = 150)
        button2 = tk.Button(self, text="Pick and Choose", bg="red", fg="black", height = 2, font = ("Helveteica 20 bold italic"), width = 15, command=lambda:[self.remove_frame(), controller.make_frame(NumPlayersGui), controller.show_frame(NumPlayersGui), controller.game.set_gamemode(1)])
        button2.place(x = 350, y = 275)
        button3 = tk.Button(self, text="Back", bg="white", font=(None, 12), command=lambda: [self.remove_frame(), controller.make_frame(MainMenu), controller.show_frame(MainMenu)])
        button3.place(x = 425, y = 400)
        button4 = tk.Button(self, text="Rules", bg="white", font=(None, 12), command=rules)
        button4.place(x = 500, y = 400)
        
    def remove_frame(self):
        self.destroy()
        #print("Frame Destroyed")
        
class NumPlayersGui(tk.Frame):   
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        player_label = tk.Label(self, text="Number Of Players",font= "Helveteica 30 bold italic", bg="black", fg="red")
        player_label.pack(pady=20, padx=20)
      
        #buttons for selecting the number of players
        button = tk.Button(self, text="2 Players", bg="red", fg="black",font = ("Helveteica 10 bold italic"), height = 2, width = 15, command=lambda:[controller.game.set_players(2),self.remove_frame(), controller.make_frame(NameOfPlayersGui), controller.show_frame(NameOfPlayersGui)])
        button.place(x = 425, y = 100)
        button = tk.Button(self, text="3 Players", bg="red", fg="black",font = ("Helveteica 10 bold italic"), height = 2, width = 15, command=lambda:[controller.game.set_players(3), self.remove_frame(), controller.make_frame(NameOfPlayersGui), controller.show_frame(NameOfPlayersGui)])
        button.place(x = 425, y = 150)
        button = tk.Button(self, text="4 Players", bg="red", fg="black",font = ("Helveteica 10 bold italic"), height = 2, width = 15, command=lambda:[controller.game.set_players(4), self.remove_frame(), controller.make_frame(NameOfPlayersGui), controller.show_frame(NameOfPlayersGui)])
        button.place(x = 425, y = 200)
        button = tk.Button(self, text="5 Players", bg="red", fg="black",font = ("Helveteica 10 bold italic"), height = 2, width = 15, command=lambda:[controller.game.set_players(5), self.remove_frame(), controller.make_frame(NameOfPlayersGui), controller.show_frame(NameOfPlayersGui)])
        button.place(x = 425, y = 250)
        button = tk.Button(self, text="6 Players", bg="red", fg="black",font = ("Helveteica 10 bold italic"), height = 2, width = 15, command=lambda:[controller.game.set_players(6), self.remove_frame(), controller.make_frame(NameOfPlayersGui), controller.show_frame(NameOfPlayersGui)])
        button.place(x = 425, y = 300)
        
        button1 = tk.Button(self, text="Back", bg="white", font=(None, 12), command=lambda: [self.remove_frame(), controller.make_frame(GameModeGui), controller.show_frame(GameModeGui)])
        button1.place(x = 460, y = 375)
        
     def remove_frame(self):
         self.destroy()
         
        
class NameOfPlayersGui(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        player_name_label = tk.Label(self, text="Names of Players",font= "Helveteica 30 bold italic", bg="black", fg="red")
        player_name_label.pack(pady=20, padx=20)
        
        entries = []
        y_axis = 100

        #creates inputs each time for how many players were selected
        for n in range(controller.game.get_players()):
            label = tk.Label(self, text="Player {}:".format(n+1), font=(None,12), bg="black", fg="red")
            label.place(x = 375, y = y_axis)
            text_in = tk.Entry(self)
            text_in.insert(0, "Player " + str(n + 1))
            text_in.place(x = 475, y = y_axis)
            entries.append(text_in)
            y_axis += 50
        
        #frame switching controls
        button1 = tk.Button(self, text="Back", bg="white", font=(None, 12), command=lambda: [self.remove_frame(), controller.make_frame(NumPlayersGui), controller.show_frame(NumPlayersGui)])
        button1.place(x = 380, y = y_axis)
        button2 = tk.Button(self, text="Next", bg="white", font=(None, 12), command=lambda: [controller.game.set_player_names(self.get_values(entries)), self.remove_frame(), controller.make_frame(GameScreenGui), controller.show_frame(GameScreenGui)])
        button2.place(x = 580, y = y_axis)
        button3 = tk.Button(self, text="Rules", bg="white", font=(None, 12), command=rules)
        button3.place(x = 480, y = y_axis)
        
    def get_values(self, entries):
       '''returns the values of each textbox'''
       names = []
       for text_box in entries:
           names.append(text_box.get()) 
       return names
      
    def remove_frame(self):
         self.destroy()
         #print("Frame Destroyed")
        
        
class GameScreenGui(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
   
        label=tk.Label(self, text = "Yahtzee", font="helvetica 40 bold italic", bg="black", fg="red")
        label.pack(pady=20, padx=20)
        label = tk.Label(self, text = "Player: " + str(controller.game.current_player),font="helvetica 15 bold italic", bg="black", fg="red")
        label.pack()
        
        categories = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Total", "Bonus", "Upper Total",\
                      "One Pair", "Two Pairs", "3 of a Kind", "4 of a Kind", "Small Straight", "Large Straight",\
                      "Full House", "YAHTZEE", "Chance", "Lower Total", "Grand Total"]
        
        category = categories[controller.game.get_round()]
        
        if controller.game.get_gamemode() == 0:
            
            categoryLabel = tk.Label(self, text = "Category: " + category, font="helvetica 15 bold italic", bg = "black", fg="red")
            categoryLabel.pack()
        
        labe2 = tk.Label(self, text = "Roll Number: " + str(controller.game.get_roll_number()), font="helvetica 15 bold italic", bg="black", fg="red")
        labe2.pack()
        img1 = tk.PhotoImage(file= self.get_image(controller.game.die1))
        img2 = tk.PhotoImage(file= self.get_image(controller.game.die2))
        img3 = tk.PhotoImage(file= self.get_image(controller.game.die3))
        img4 = tk.PhotoImage(file= self.get_image(controller.game.die4))
        img5 = tk.PhotoImage(file= self.get_image(controller.game.die5))
        
        #this code keeps the buttons as locked even when the new frames are made
        if controller.game.die1.get_locked():
            hold_text1 = "Locked"
        else:
            hold_text1 = "Hold"
        if controller.game.die2.get_locked():
            hold_text2 = "Locked"
        else:
            hold_text2 = "Hold"
        if controller.game.die3.get_locked():
            hold_text3 = "Locked"
        else:
            hold_text3 = "Hold"
        if controller.game.die4.get_locked():
            hold_text4 = "Locked"
        else:
            hold_text4 = "Hold"
        if controller.game.die5.get_locked():
            hold_text5 = "Locked"
        else:
            hold_text5 = "Hold"
        
        #loads the pictures for the dice
        dice1 = tk.Label(self, image=img1, bd = 0)
        dice1.image = img1
        dice1.place(x = 75, y = 200)
        
        dice2 = tk.Label(self, image=img2, bd = 0)
        dice2.image = img2
        dice2.place(x = 250, y = 200)
        
        dice3 = tk.Label(self, image=img3, bd = 0)
        dice3.image = img3
        dice3.place(x = 425, y = 200)
        
        dice4 = tk.Label(self, image=img4, bd = 0)
        dice4.image = img4
        dice4.place(x = 600, y = 200)
        
        dice5 = tk.Label(self, image=img5, bd = 0)
        dice5.image = img5
        dice5.place(x = 775, y = 200)
        
        #buttons for locking the dice
        hold_1_button = tk.Button(self, text = hold_text1, bg="red", fg="white", font= "Helveteica 10 bold italic", command=lambda: [btn_swap(hold_1_button), controller.game.set_Locked_Dice(0, hold_1_button['text']), controller.game.die1.toggle_lock()])
        hold_1_button.place(x = 125, y =365)
        hold_2_button = tk.Button(self, text = hold_text2, bg="red", fg="white", font= "Helveteica 10 bold italic", command=lambda: [btn_swap(hold_2_button), controller.game.set_Locked_Dice(1, hold_2_button['text']), controller.game.die2.toggle_lock()])
        hold_2_button.place(x = 300, y =365)
        hold_3_button = tk.Button(self, text = hold_text3, bg="red", fg="white", font= "Helveteica 10 bold italic", command=lambda: [btn_swap(hold_3_button), controller.game.set_Locked_Dice(2, hold_3_button['text']), controller.game.die3.toggle_lock()])
        hold_3_button.place(x = 475, y =365)
        hold_4_button = tk.Button(self, text = hold_text4, bg="red", fg="white", font= "Helveteica 10 bold italic", command=lambda: [btn_swap(hold_4_button), controller.game.set_Locked_Dice(3, hold_4_button['text']), controller.game.die4.toggle_lock()])
        hold_4_button.place(x = 650, y =365)
        hold_5_button = tk.Button(self, text = hold_text5, bg="red", fg="white", font= "Helveteica 10 bold italic", command=lambda: [btn_swap(hold_5_button), controller.game.set_Locked_Dice(4, hold_5_button['text']), controller.game.die5.toggle_lock()])
        hold_5_button.place(x = 825, y =365)
        
        roll_button = tk.Button(self, text="Roll", bg="red", fg="black", font= "Helveteica 15 bold italic", state = "normal" if controller.game.get_roll_number() != 3 else "disabled", command=lambda: [controller.game.roll_dice(), controller.game.update_roll_number(), self.remove_frame(), controller.make_frame(GameScreenGui), controller.show_frame(GameScreenGui)])
        roll_button.place(x=275, y=450)
            
        end_turn_button = tk.Button(self, text="End Turn", bg="red", fg="black", font= "Helveteica 15 bold italic", command=lambda: [controller.game.unlock_dice(), controller.game.set_display(), controller.game.show_buttons_true(),controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui), self.remove_frame()])
        end_turn_button.place(x=625, y=450)      
        
        rules_button = tk.Button(self,  bg="white", text="Rules",font=(None, 12), command=rules)
        rules_button.place(x=540, y=525)  
        
        scoreboard_button = tk.Button(self,  bg="white", text="Display Scoreboard", font=(None, 12), command=lambda: [self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)])
        scoreboard_button.place(x= 375, y = 525)
        
        def btn_swap(button):
          if button['text'] == "Hold":  
              button.config(text="Locked")
          else:
              button.config(text="Hold")            
        
    def get_image(self, die):        
        if die.get_value() == 1:
            return "die 1.gif" 
        elif die.get_value() == 2:
            return "die 2.gif"
        elif die.get_value() == 3:
            return "die 3.gif"
        elif die.get_value() == 4:
            return "die 4.gif"
        elif die.get_value() == 5:
            return "die 5.gif"
        elif die.get_value() == 6:
            return "die 6.gif"
          
    def remove_frame(self):
         self.destroy()
       
            
class DisplayScoreboardGui(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        
        categories = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Total", "Bonus", "Upper Total",\
                      "One Pair", "Two Pairs", "3 of a Kind", "4 of a Kind", "Small Straight", "Large Straight",\
                      "Full House", "YAHTZEE", "Chance", "Lower Total", "Grand Total"]
        players = controller.game.get_player_names()
        
        scoreboard = tk.Label(self, text = "Scoreboard", bg = "black", fg = "red", font = "helveteica 25 bold italic")
        scoreboard.grid(row = 0, column = 2, columnspan = 2)
        
        #decides which scoreboard to show based off the gamemode and if they've already picked their score
        if (controller.game.get_gamemode() == 0) or (controller.game.show_buttons == False):
            header = tk.Label(self, text = "Category", bg = "red", fg = "black", font = "helveteica 10 bold italic", height = 2, width = 15, bd = 1, relief = "solid")
            header.grid(row = 1, column = 1)
            
            row = 2
            
            #shows categories
            for category in categories:   
                newLabel1 = tk.Label(self, text = category, bg = "red", fg = "black", font = "helveteica 10 bold italic", height = 1, width = 15, bd = 1, relief = "solid")
                newLabel1.grid(row = row, column = 1)
                row += 1
            
            column = 2
            category = controller.game.get_round()
            if controller.game.get_gamemode() == 0:
                controller.game.scoreboard.set_score(categories[category])
            
            #places selectable buttons for the scoreboard
            place_button = 0
            for player in players:
                newLabel1 = tk.Label(self, text = player, bg = "red", fg = "black", font = "helveteica 10 bold italic", height = 2, width = 15, bd = 1, relief = "solid")
                newLabel1.grid(row = 1, column = column)
                for x in range(len(categories)):
                    if player.scores[categories[x]] >= 0:
                        emptyLabel = tk.Label(self, text=str(player.scores[categories[x]]), bg = "red", height = 1, width = 15)
                    else:
                        emptyLabel = tk.Label(self, text="-", bg = "red", height = 1, width = 15)
                    emptyLabel.grid(row = x + 2, column = column)
                column += 1
                place_button += 65
            
            #changes the button  depending if the game is over, game is ongoing, or user selected the show scoreboard button
            if (category == 17) and (controller.game.current_player == players[len(players) - 1]):
                button1 = tk.Button(self, text = "Display Winner",  font = "helveteica 12 bold italic", command =lambda: [controller.make_frame(DisplayWinnerGui), controller.show_frame(DisplayWinnerGui), self.remove_frame()])
                button1.place(x = place_button, y = 525)
            elif controller.game.display == True:
                button1 = tk.Button(self, text = "New Player Turn",  font = "helveteica 12 bold italic", command =lambda: [controller.game.set_round(), controller.game.set_display(), controller.game.show_buttons_flip(), controller.game.roll_dice(), controller.game.next_player(), controller.game.set_roll_number(), self.remove_frame(), controller.make_frame(GameScreenGui), controller.show_frame(GameScreenGui)])
                button1.place(x = place_button, y = 525)
            else:
                button1 = tk.Button(self, text = "Back",  font = "helveteica 12 bold italic", command =lambda: [self.remove_frame(), controller.make_frame(GameScreenGui), controller.show_frame(GameScreenGui)])
                button1.place(x = place_button, y = 525)
            
        else:
            
            header = tk.Label(self, text = "Category", bg = "red", fg = "black", font = "helveteica 10 bold italic", height = 2, width = 15, bd = 1, relief = "solid")
            header.grid(row = 1, column = 1)
            
            row = 2
        
            scores = controller.game.current_player.get_scores()
            
            #shows each category of the scoreboard
            button1 = tk.Button(self, text="Ones", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Ones"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Ones']!=-1 else "normal")
            button1.grid(row = 2, column = 1)
            button2 = tk.Button(self, text="Twos", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Twos"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Twos']!=-1 else "normal")
            button2.grid(row = 3, column = 1)
            button3 = tk.Button(self, text="Threes", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Threes"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Threes']!=-1 else "normal")
            button3.grid(row = 4, column = 1)
            button4 = tk.Button(self, text="Fours", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Fours"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Fours']!=-1 else "normal")
            button4.grid(row = 5, column = 1)
            button5 = tk.Button(self, text="Fives", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Fives"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Fives']!=-1 else "normal")
            button5.grid(row = 6, column = 1)
            button6 = tk.Button(self, text="Sixes", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Sixes"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Sixes']!=-1 else "normal")
            button6.grid(row = 7, column = 1)
            label1 = tk.Label(self, text="Total", bg = "red", height = 1, width = 15, bd = 2, relief = "solid")
            label1.grid(row = 8, column = 1)
            label2 = tk.Label(self, text="Bonus", bg = "red", height = 1, width = 15, bd = 2, relief = "solid")
            label2.grid(row = 9, column = 1)
            label3 = tk.Label(self, text="Upper Total", bg = "red", height = 1, width = 15, bd = 2, relief = "solid")
            label3.grid(row = 10, column = 1)
            button7 = tk.Button(self, text="One Pair", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("One Pair"), controller.game.show_buttons_flip(),  self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['One Pair']!=-1 else "normal")
            button7.grid(row = 11, column = 1)
            button7 = tk.Button(self, text="Two Pairs", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Two Pairs"), controller.game.show_buttons_flip(),  self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Two Pairs']!=-1 else "normal")
            button7.grid(row = 12, column = 1)
            button7 = tk.Button(self, text="3 of a Kind", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("3 of a Kind"), controller.game.show_buttons_flip(),  self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['3 of a Kind']!=-1 else "normal")
            button7.grid(row = 13, column = 1)
            button8 = tk.Button(self, text="4 of a Kind", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("4 of a Kind"), controller.game.show_buttons_flip(),  self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['4 of a Kind']!=-1 else "normal")
            button8.grid(row = 14, column = 1)
            button10 = tk.Button(self, text="Small Straight", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Small Straight"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Small Straight']!=-1 else "normal")
            button10.grid(row = 15, column = 1)
            button11 = tk.Button(self, text="Large Straight", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Large Straight"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Large Straight']!=-1 else "normal")
            button11.grid(row = 16, column = 1)
            button9 = tk.Button(self, text="Full House",  bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Full House"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Full House']!=-1 else "normal")
            button9.grid(row = 17, column = 1)
            button12 = tk.Button(self, text="YAHTZEE", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("YAHTZEE"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['YAHTZEE']!=-1 else "normal")
            button12.grid(row = 18, column = 1)
            button13 = tk.Button(self, text="Chance", bg="white", height = 1, width = 15, command=lambda: [controller.game.scoreboard.set_score("Chance"), controller.game.show_buttons_flip(), self.remove_frame(), controller.make_frame(DisplayScoreboardGui), controller.show_frame(DisplayScoreboardGui)], state="disabled" if scores['Chance']!=-1 else "normal")
            button13.grid(row = 19, column = 1)
            label4 = tk.Label(self, text="Lower Total", bg = "red", height = 1, width = 15, bd = 2, relief = "solid")
            label4.grid(row = 20, column = 1)
            label5 = tk.Label(self, text="Grand Total", bg = "red", height = 1, width = 15, bd = 2, relief = "solid")
            label5.grid(row = 21, column = 1)
            
            #shows the player portion of the scoreboard
            column = 2
            distance = 200
            for player in players:
                newLabel1 = tk.Label(self, text = player, bg = "red", fg = "black", font = "helveteica 10 bold italic", height = 2, width = 15, bd = 1, relief = "solid")
                newLabel1.grid(row = 1, column = column)
                for x in range(len(categories)):
                    if player.scores[categories[x]] >= 0:
                        emptyLabel = tk.Label(self, text=str(player.scores[categories[x]]), bg = "red", height = 1, width = 15)
                    else:
                        emptyLabel = tk.Label(self, text="-", bg = "red", height = 1, width = 15)
                    emptyLabel.grid(row = x + 2, column = column)
                column += 1
                distance += 112
           
            dievaluesLabel = tk.Label(self, text = "Dice Score", font = "helveteica 15 bold italic", bg = "black", fg = "red")
            dievaluesLabel.place(x = distance, y = 200)
            diceLabel = tk.Label(self, text = str(controller.game.die1)+ "-"  + str(controller.game.die2) +  "-" + str(controller.game.die3) + "-" + str(controller.game.die4) + "-" +str(controller.game.die5), bg = "black", font = "helveteica 15 bold italic", fg = "red")
            diceLabel.place(x = distance, y = 225)
    
    def remove_frame(self):
        self.destroy()
        
   
class DisplayWinnerGui(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        
        winner_header=tk.Label(self, text = "Congratulations!", font=(None, 50), bg="Black", fg="red")
        winner_header.pack(padx=20, pady=20)
        
        winner = self.controller.game.scoreboard.calculate_winner()
        
        winner_label = tk.Label(self, text = winner[0] + " won with " + str(winner[1]) + " points!", font=(None, 20), bg="black", fg="red")
        winner_label.pack(padx=20, pady=20)
        
        img = tk.PhotoImage(file="crown.gif")
        crown = tk.Label(self, image=img, bd = 0, bg = "black")
        crown.image = img
        crown.place(x = 300, y = 180)
        
        rematch_button = tk.Button(self,  bg="white", text="Rematch", font=(None, 15), command=lambda: [controller.game.rematch(), self.remove_frame(), controller.make_frame(GameScreenGui), controller.show_frame(GameScreenGui)])
        rematch_button.place(x=350, y=500)
        
        new_game_button = tk.Button(self,  bg="white", text="New Game", font=(None, 15), command=lambda: [ controller.game.reset(), self.remove_frame(), controller.make_frame(GameModeGui), controller.show_frame(GameModeGui)])
        new_game_button.place(x=550, y=500)
        
    def remove_frame(self):
        self.destroy()       
        
def rules():
    '''makes a popup of the rules for the players to read'''
    rules = open("rules.txt", "r").read().strip()
    
    popup = tk.Tk()
    popup.wm_title("Rules")
    label = tk.Label(popup, text=rules, font=(None,9), anchor = "w")
    label.pack() 
    
    button1 = tk.Button(popup, text="Back", command=popup.destroy)
    button1.pack()
    
    popup.mainloop()
