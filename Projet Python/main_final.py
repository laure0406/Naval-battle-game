"""
    main_final
    ----------
Commencé le 8/04/21

Auteur: Alix and Laure
Role: Programme principal.

Points critiques: affichage des grilles avec l'interface graphique. 
(Utilisation de PySimpleGUI CookBook.)

Terminé le 12/05/21 
 
"""

import PySimpleGUI as sg
from random import randint
from fonctions_finales import *
sg.theme('Dark Teal 7') #Thème des couleurs choisies pour notre interface graphique.
MAX_ROWS=MAX_COL=11
layout=[
        #mise en place du bouton pour lancer la partie puis mise en place du titre'bataille navale' ainsi que le score du joueur et de l'ordi
        [sg.Button('Lancer le jeu', size=(10,2), pad=(1,12), key="Lancer")],
        [sg.Text('Bataille Navale', font=('Arial', 20), key='titre',pad =(340,50),)],
        [sg.Text('Score Joueur :', font=('Arial', 14), key='scoreJoueur', pad =(5,5)),sg.Text(" "*10, key='scoreJ')],
        [sg.Text('Score Ordinateur :', font=('Arial', 14), key='score Ordi', pad =(5,5)),sg.Text(" "*10,key='scoreO')],
        #mise en place de la grille du joueur
        [sg.Frame("Joueur",font=('Calibri',17), title_location='n',layout=[
        [sg.Button(button_color=('#009ED9', '#009ED9'),size=(2,1),key=(i,j,1), pad=(0,0))
        for j in range(MAX_COL)] for i in range(MAX_ROWS)],),
        #mise en place de la console
        sg.Frame("Console",font=('Calibri',14),layout=[
        [sg.Output(size=(40,18), key='-OUTPUT-')]], vertical_alignment="top", title_location='n'),
        #mise en place de la grille de tir, grille où se trouve les bateaux de l'ordinateur
        sg.Frame("Ordinateur",font=('Calibri',17), title_location='n',layout=[
        [sg.Button(button_color=('#009ED9', '#009ED9'),size=(2,1),key=(i,j,0), pad=(0,0))
        for j in range(MAX_COL)] for i in range(MAX_ROWS)],),
        ],
        #mise en place du bouton pour quitter la partie
        [sg.Button('Quitter la partie', key="Quitter")],

        ]

# Creation de la fenetre layout
window=sg.Window('Bataille Navale', layout=layout,grab_anywhere=True)

#initialisation de toutes les variables dont on va avoir besoin tout au long du code

#variable qui compte le score des joueurs
score_joueur = 25
score_ordi =25
#matrice 2*2 qui prend en compte l'état de la case de la grille du joueur:
#libre: pas de bateau/occupé: bateau placé sur cette case
etat_mer = [['libre' for a in range(MAX_COL)] for b in range(MAX_ROWS)]
mer_ordi = [['libre' for a in range(MAX_COL)] for b in range(MAX_ROWS)]
#matrice 2*2 qui enregistre les cases où à tirer l'ordinateur
tirer = [[0 for a in range(MAX_COL)] for b in range(MAX_ROWS)]
#compteur des bateaux placés chez le joueur
cpt_joueur = 0
#compteur des bateaux placés chez l'ordinateur
cpt_ordi =0
#variables qui nous permettent de placer les bateaux du joueur
n=0
nbr =0
bateau=[2,3,3,4,5]
bateaux_placer=[0]*6
e=0
#variables qui nous permettent de compter les bateaux touchés des joueurs
cpt_fin_ordi=0
cpt_fin_joueur=0
#variable qui nous permet d'afficher 'vous pouvez jouer' une seule fois dans le jeu
affichage_popup_unique=1
#variable pour fin de partie et gestion des scores
scores=[0]*100
pseudos=[""]*100

while True :
    event, values = window.read() # lecture du dernier évenement
    print(event, values)
    if (event == sg.WIN_CLOSED) or (event =="Quitter"): # si "quitter", on casse la boucle
        window.close()
        break

#si le joueur clique sur le bouton Lancer la partie, la partie se lance.
    if event == "Lancer":
        sg.popup('Bienvenue dans votre Bataille Navale !','\n Veuillez placer vos bateaux.')
    event, window = numerotation(event, window)

#tant que l'ordinateur n'a pas placé ses 5 bateaux on lui demande de les placer
    while cpt_ordi<5:
        mer_ordi,cpt_ordi,nbr = placement_ordi(event,window,mer_ordi,bateau,cpt_ordi,nbr)
#si le joueur n'a pas placé tous ses bateaux on lui demande de les placer
    if cpt_joueur<5:
        event,window,etat_mer,cpt_joueur,bateaux_placer,e = choix_bateau(event,window,etat_mer,cpt_joueur,bateaux_placer,e)

#si tous les bateaux sont placés, alors on peut commencer à jouer
    if (cpt_ordi==5) and (cpt_joueur==5) and affichage_popup_unique==1:
        sg.popup('Vous pouvez commencer à jouer!')
        affichage_popup_unique=0 #comme la variable ne sera plus jamais égale à 1, le message n'apparaitra qu'une seule fois

# on passe au jeu, si tous les bateaux sont placés et que le score des 2 joueurs est supérieur à 0 on continue à jouer
    if (cpt_ordi==5) and (cpt_joueur==5):
         event, window,score_joueur, score_ordi, etat_mer, mer_ordi, tirer,cpt_fin_joueur,cpt_fin_ordi= tour_joueur(event,window,mer_ordi, etat_mer,score_joueur,score_ordi, tirer, cpt_fin_joueur, cpt_fin_ordi, pseudos, scores)
         
         #erreur dans l'appel de fonction, ordre: mer_ordi, etat_mer, score_joueur, score_ordi,
         

       
         
         