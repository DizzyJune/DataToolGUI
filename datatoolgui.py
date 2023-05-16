import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

Menu = Tk()
Menu.title('DataToolGUI')
Menu.geometry('800x500')

HeroOptions = [
"Select Hero",
"Ana",
"Ashe",
"Baptiste",
"Bastion",
"Brigitte",
"Cassidy",
"D.Va",
"Doomfist",
"Echo",
"Genji",
"Hanzo",
"Junker Queen",
"Junkrat",
"Kiriko",
"Lifeweaver",
"Lucio",
"Mei",
"Mercy",
"Moira",
"Orisa",
"Pharah",
"Ramattra",
"Reaper",
"Reinhardt",
"Roadhog",
"Sigma",
"Sojourn",
"Soldier: 76",
"Sombra",
"Symmetra",
"Torbjorn",
"Tracer",
"Widowmaker",
"Winston",
"Wrecking Ball",
"Zarya",
"Zenyatta"
]

variable = StringVar(Menu)
variable.set(HeroOptions[0])

def ExtractSkin():
    inputhero = variable.get()
    inputskin = skininput.get()
    dir_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dir_path)
    os.system(fr'datatool.exe "D:\Overwatch" extract-unlocks "D:\DataTool\Exports" "{inputhero}|skin={inputskin}"')

MenuTitle = ttk.Label(Menu, text = 'DataToolGUI', font = 'Calibri 80 bold')
MenuTitle.pack(pady = -20)
disclaimer = ttk.Label(Menu, text = "Disclaimer: You must run this in the same directory as Datatool.exe!", font = 'Calibri 20')
disclaimer.pack()

heroframe = ttk.Frame(Menu)
#entrylabel = ttk.Label(heroframe, text = "Hero", font = 'Calibri 25')
#entrylabel.pack(side = 'left', padx = '10')
inputoption = ttk.OptionMenu(heroframe, variable, *HeroOptions)
inputoption.config(width = 13)
inputoption.pack(ipady=5)
heroframe.pack(pady = '5')

skinframe = ttk.Frame(Menu)
skinlabel = ttk.Label(skinframe, text = "Skin", font = 'Calibri 25')
skinlabel.pack(side = 'left', padx = '16')
skininput = ttk.Entry(skinframe, font = 'Calibri 20')
skininput.pack(side = 'left')
skinframe.pack()

pathsframe = ttk.Frame(Menu)
toolpathlabel = ttk.Label(pathsframe, text = "Datatool.exe Path", font = 'Calibri 25')

ExportButton = ttk.Button(Menu, text = "Export", command = ExtractSkin, width = 20)
ExportButton.pack()

Menu.mainloop()