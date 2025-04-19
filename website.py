'''
Author: Aayan Ahmad Khan
Date: 14/04/2025
Info: PokeDex that tells information about a Pokemon.
'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import requests
import webbrowser
import random
import io
import pyttsx3

def poke_info():
    get = entry_1.get().strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{get}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name']
        height = data['height']
        weight = data['weight']
        types = [type['type']['name'] for type in data['types']]
        sprite_url = data['sprites']['front_default']

        info = f"Name: {name.capitalize()}, Height: {height}\nWeight: {weight}, Types: {', '.join(types)}"

        label1 = Label(root, text=info, font=("Arial", 7), bg="green", fg="black", justify=LEFT)
        label1.place(x=240, y=165)

        if sprite_url:
            img_response = requests.get(sprite_url)
            img_data = img_response.content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((96, 96))
            photo = ImageTk.PhotoImage(img)

            label_img = Label(root, image=photo, bg="white")
            label_img.image = photo
            label_img.place(x=60, y=135)
        else:
            error_label = Label(root, text="🔴Image not available🔴", font=("Arial", 8), bg="white", fg="black")
            error_label.place(x=50, y=150)
    else:
         error_label2 = Label(root, text="🔴Pokemon not available🔴", font=("Arial", 7), bg="white", fg="black")
         error_label2.place(x=45, y=170)
    
root = tk.Tk()
root.title("PokeDex")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="white")

image = Image.open("poekdex.png")
image = image.resize((400, 400))
photo = ImageTk.PhotoImage(image)

img_label = Label(root, image=photo)
img_label.pack(pady=10)

title_label = Label(root,text="PokeDex",font=("Arial", 24, "bold"),bg="white", fg="red")
title_label.place(x=240, y=10)

entry_1 = Entry(root, width=20, font=("Arial", 8), bg="green", fg="black")
entry_1.place(x=240, y=145)
entry_1.insert(0, "Enter Pokémon name...")

def on_entry_click(event):
    if entry_1.get() == "Enter Pokémon name...":
        entry_1.delete(0, "end")
        entry_1.config(fg="white")

def poke_talk():
    get = entry_1.get().strip().lower()
    if get == "":
        print("Please enter a Pokémon name.")
        return
    url = f"https://pokeapi.co/api/v2/pokemon/{get}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        types = [t['type']['name'].capitalize() for t in data['types']]

        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{get}"
        species_response = requests.get(species_url)
        
        if species_response.status_code == 200:
            species_data = species_response.json()
            
            description = next(
                (entry['flavor_text'] for entry in species_data['flavor_text_entries'] if entry['language']['name'] == 'en'),
                "No description available."  
            )
            description = description.replace("\n", " ").replace("\f", " ") 

        
            type_text = " and ".join(types) if len(types) > 1 else types[0] 
            pokedex_sentence = f"{name}, an {type_text}-type Pokémon. {description}"  

            engine = pyttsx3.init()
            engine.say(pokedex_sentence)
            engine.runAndWait() 
        else:
            print("Pokédex description not found.")
    else:
        print("Pokemon not found.")

entry_1.bind("<FocusIn>", on_entry_click)

button1 = Button(root, text="Search", font=("Arial", 10), bg="black", fg="red", command=poke_info)
button1.place(x=240, y=275)

button2 = Button(root, text="PokeTalk", font=("Arial", 9), bg="grey", fg="yellow", command=poke_talk)
button2.place(x=240, y=324)

def change_color():
    colors = ["#FF073A", "#FF6F00", "#FFFF00", "#39FF14", "#1B03A3", "#FF10F0", "#9B4DFF", "#00FFFF", "#FF00FF", "#32CD32"]
    Devlabel["fg"] = random.choice(colors)
    title_label["fg"] = random.choice(colors)
    root.after(300, change_color)

def goweb():
    if Devlabel:
        webbrowser.open("https://github.com/ProfessorDev786")

Devlabel = Button(root, text="MADE by: ProfessorDev π", bg="black", bd=0, command=goweb, font=("Impact", 10))
Devlabel.place(x=260, y=380)

change_color()
root.mainloop()
