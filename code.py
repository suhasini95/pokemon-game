from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Endless pokemon game")
root.geometry("800x600")
root.configure(background = "yellow2")

img = ImageTk.PhotoImage(Image.open("button.jpg"))

pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
Charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
Squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
Ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
Persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
pokemon_list = [pikachu,bulbasour,Iyvasour,Charmender,Squirtle,Ratata,jigglypuff,meowth,Persion,abra,kadabra]
pokemon_power_list = [200,60,100,50,50,40,70,60,70,30,70]

player1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)
              
player_1_score_label = Label(root, bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

label = Label(root)
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

player1_score = 0
def player1():
    global player1_score
    random1 = random.randint(0,10)
    random_pokemon = pokemon_list[random1]
    label["image"] = random_pokemon
    random_power_list = pokemon_power_list[random1]
    player1_score = player1_score + random_power_list
    player_1_score_label["text"] = str(player1_score)
  
player1_button = Button(root, image = img, command = player1)
player1_button.place(relx = 0.1, rely = 0.6, anchor = CENTER)

player2_score = 0
def player2():
    global player2_score
    random2 = random.randint(0,10)
    random_pokemon = pokemon_list[random2]
    label["image"] = random_pokemon
    random_power_list = pokemon_power_list[random2]
    player2_score = player2_score + random_power_list
    player_2_score_label["text"] = str(player2_score)
    
player2_button = Button(root, image = img, command = player2)
player2_button.place(relx = 0.9, rely = 0.6, anchor = CENTER)
        
root.mainloop()