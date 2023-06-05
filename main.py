# this is part of the WaitePath project.
#
# Release: v1.0-dev8
#
# Copyright (c) 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez


import os
import base64
import io
import random
import time

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from src.images import *


"""site to encode images in base64 https://base64.guru/converter/encode/image"""

window = Tk()
window.title("WaitePath")
window.geometry("1200x650")
window.resizable(False, True)# False for non-responsive window and True for responsive.
window.attributes('-alpha',9.1)
#window['background'] = '#373636'
#foto_icon = PhotoImage(data=base64.b64decode(ICON_LOGO))
#window.iconphoto(True, foto_icon)


image_data = base64.b64decode(image_background_base64)
img = PhotoImage(data=image_data)


background_label = Label(window, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



def start_game():
    
    palavras = [CARD1_MAGICIAN, 
                CARD2_2_DE_ESPADAS, 
                CARD3_RAINHA_DE_OUROS, 
                CARD4_AS_DE_COPAS, 
                CARD5_O_PENDURADO, 
                CARD6_3_DE_PAUS,
                CARD7_OS_ENAMORADOS,
                CARD8_10_DE_COPAS,]
    
    palavras_aleatorias = random.sample(palavras, 5)


    while len(set(palavras_aleatorias)) < 5:
        palavras_aleatorias = random.sample(palavras, 5)

    #print(palavras_aleatorias[1])

    # casa 1
    time.sleep(0.1)
    window.update_idletasks()
    bg1 = PhotoImage(data=base64.b64decode(palavras_aleatorias[0]))
    label = Label(window, image=bg1)
    label.place(x = 100,y = 200)
        
    #casa 2
    time.sleep(0.1)
    window.update_idletasks()
    bg2 = PhotoImage(data=base64.b64decode(palavras_aleatorias[1]))
    label = Label(window, image=bg2)
    label.place(x = 750,y = 200)
        
    #casa 3 
    time.sleep(0.1)
    window.update_idletasks()
    bg3 = PhotoImage(data=base64.b64decode(palavras_aleatorias[2]))
    label = Label(window, image=bg3)
    label.place(x = 450,y = 10)
        
    #casa 4
    time.sleep(0.1)
    window.update_idletasks()
    bg4 = PhotoImage(data=base64.b64decode(palavras_aleatorias[3]))
    label = Label(window, image=bg4)
    label.place(x = 370,y = 460)
        
    #casa 5
    time.sleep(0.1)
    window.update_idletasks()
    bg5 = PhotoImage(data=base64.b64decode(palavras_aleatorias[4]))
    label = Label(window, image=bg5)
    label.place(x = 400,y = 240)
    window.mainloop()


COLOR_BUTTON = '#191A1A'
COLOR_LETTER = '#00E9CA'

botao = Button(window,
                text="Start",
                command=start_game,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,).place(x=800, y=600)
        
if __name__ == "__main__":
    window.mainloop()