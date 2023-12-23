# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:36:04 2023

@author: bryso
"""

import tkinter as tk
from random import choice

# Dictionary of colors
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]

def change_background_color():
    # Pick a random color from the dictionary
    new_color = choice(colors)
    
    # Update the background color of the root window
    root.configure(bg=new_color)

# Create the main window
root = tk.Tk()
root.title("Random Background Color Changer")

# Create a button to change the background color
change_color_button = tk.Button(root, text="Change Color", command=change_background_color)
change_color_button.pack(pady=10)

# Set initial background color
root.configure(bg="white")

# Run the Tkinter event loop
root.mainloop()
