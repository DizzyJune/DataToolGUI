import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import configparser
import sys

Menu = Tk()
Menu.title('DataToolGUI')
Menu.geometry('800x500')

config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'datatoolguiconfig.ini')
if os.path.exists(config_file):
    config.read(config_file)
    owpath = config['PATHS']['owpath']
    exportpath = config['PATHS']['exportpath']
    toolexec = config['PATHS']['toolexec']
else:
    owpath = ''
    exportpath = ''
    toolexec = ''

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
    toolpath = toolexecinput.get()
    os.chdir(toolpath)

    config = configparser.ConfigParser()
    config['PATHS'] = {
        'owpath': owpathinput.get(),
        'exportpath': exportpathinput.get(),
        'toolexec': toolexecinput.get()
    }
    with open('datatoolguiconfig.ini', 'w') as configfile:
        config.write(configfile)

    os.system(fr'datatool.exe "{owpathinput.get()}" extract-unlocks "{exportpathinput.get()}" "{inputhero}|skin={inputskin}"')


MenuTitle = ttk.Label(Menu, text='DataToolGUI', font='Calibri 80 bold')
MenuTitle.pack(side='top')

heroframe = ttk.Frame(Menu)
inputoption = ttk.OptionMenu(heroframe, variable, *HeroOptions)
inputoption.config(width = 13)
inputoption.pack(ipady=5)
heroframe.pack(pady = '5')

owfilespath = ttk.Frame(Menu)
owpathlabel = ttk.Label(owfilespath, text = "Overwatch Files Path", font = 'Calibri 20')
owpathinput = ttk.Entry(owfilespath, font = 'Calibri 17')
owpathinput.insert(0, owpath)
exportpathlabel = ttk.Label(owfilespath, text = "Export Path", font = 'Calibri 20')
exportpathinput = ttk.Entry(owfilespath, font = 'Calibri 17')
exportpathinput.insert(0, exportpath)
skinlabel = ttk.Label(owfilespath, text = "Skin", font = 'Calibri 20')
skininput = ttk.Entry(owfilespath, font = 'Calibri 17')
toolexeclabel = ttk.Label(owfilespath, text = 'DataTool.exe Path', font = 'Calibri 20')
toolexecinput = ttk.Entry(owfilespath, font = 'Calibri 17')
toolexecinput.insert(0, toolexec)
skinlabel.grid(row=0, column=0, padx=10, pady=10)
skininput.grid(row=0, column=1, padx=10, pady=10)
owpathlabel.grid(row=1, column=0, padx=10, pady=10)
owpathinput.grid(row=1, column=1, padx=10, pady=10)
exportpathlabel.grid(row=2, column=0, padx=10, pady=10)
exportpathinput.grid(row=2, column=1, padx=10, pady=10)
toolexeclabel.grid(row=3, column=0, padx=10, pady=10)
toolexecinput.grid(row=3, column=1, padx=10, pady=10)
owfilespath.pack()

ExportButton = ttk.Button(Menu, text = "Export", command = ExtractSkin, width = 20)
ExportButton.pack(pady = 10)

Menu.mainloop()