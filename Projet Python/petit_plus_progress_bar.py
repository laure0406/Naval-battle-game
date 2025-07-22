# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:15:50 2021

@author: laumu
"""

import PySimpleGUI as sg

BAR_MAX=1000
layout=[
        [sg.Frame("Statuts Bateaux",font=('Calibri',17), title_location='n',layout=[
          [sg.Text('Porte-Avion',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG1-')],
          [sg.Text('Croiseur',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG2-')],
          [sg.Text('Contre-Torpieur 1',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG3-')],
          [sg.Text('Contre-Torpieur 2',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG4-')],
          [sg.Text('Sous-Marin',font=("Arial",8))],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,10), key='-PROG5-')],])]
          ]
         
window=sg.Window('Bataille Navale', layout=layout,grab_anywhere=True)
          
        
while True :
    event, values = window.read() # lecture du dernier évenement
    print(event, values)
    if (event == sg.WIN_CLOSED) or (event =="Quitter"): # si "quitter", on casse la boucle
        window.close()
        break