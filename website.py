'''
Author: Aayan Ahmad Khan
Date: 14/04/2025
Info: PokeDex that tells information about a Pokemon.
'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import requests

def poke_info():
    get = entry_1.get()
    url = f"https://pokeapi.co/api/v2/pokemon/{get}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        height = data['height']
        weight = data['weight']
        types = [type['type']['name'] for type in data['types']]
        info = f"Name: {name}\nHeight: {height}\nWeight: {weight}\nTypes: {', '.join(types)}"
        label1 = Label(root, text=info, font=("Arial", 10), bg="white", fg="black")
        label1.place(x=70, y=150)
    else:
        print("Pokemon not found.")
        
root = Tk()
root.title("PokeDex")
root.geometry("400x400")

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

entry_1.bind("<FocusIn>", on_entry_click)

button1 = Button(root, text="Search", font=("Arial", 10), bg="black", fg="red", command=poke_info)
button1.place(x=240, y=275)

root.mainloop()