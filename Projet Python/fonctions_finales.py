# -*- coding: utf-8 -*-
"""
    fonctions_finales
    -----------------

Commencé le 13/04/21

Auteur: Alix et Laure
Role: Programme contenant toutes les fonctions qui font tourner le jeu.
Points critiques: 
    ► placement_bateau
    ► tour_ordi et tour_joueur
(Utilisation de PySimpleGUI, CookBook.)

Terminé le 12/05/21 
"""
import PySimpleGUI as sg 
from random import randint

#Alix
#fonction marche parfaitement
def numerotation(event, window):
    """
    Parameters
    ----------
    event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer
    
    Role
    ----
    la fonction permet d'afficher les numéros des cases et des lignes de la grille du joueur et de celle de l'ordi.
    Returns
    -------
    event : le clique du joueur, de type 'non-type'    
    window : la fenêtre mise à jour (après l'ajout des numéros)

    """
    #numérotation joueur
    #chiffres sur la premiere colonne
    for i in range(2):
        window[(0,0,i)].Update('')
        window[(1,0,i)].Update('1',button_color = ('black', '#F3F9A6'))
        window[(2,0,i)].Update('2',button_color = ('black', '#F3F9A6'))
        window[(3,0,i)].Update('3',button_color = ('black', '#F3F9A6'))
        window[(4,0,i)].Update('4',button_color = ('black', '#F3F9A6'))
        window[(5,0,i)].Update('5',button_color = ('black', '#F3F9A6'))
        window[(6,0,i)].Update('6',button_color = ('black', '#F3F9A6'))
        window[(7,0,i)].Update('7',button_color = ('black', '#F3F9A6'))
        window[(8,0,i)].Update('8',button_color = ('black', '#F3F9A6'))
        window[(9,0,i)].Update('9',button_color = ('black', '#F3F9A6'))
        window[(10,0,i)].Update('10',button_color = ('black', '#F3F9A6'))
        
        #lettre sur la première ligne
        window[(0,1,i)].Update('A',button_color = ('black', '#F3F9A6'))
        window[(0,2,i)].Update('B',button_color = ('black', '#F3F9A6'))
        window[(0,3,i)].Update('C',button_color = ('black', '#F3F9A6'))
        window[(0,4,i)].Update('D',button_color = ('black', '#F3F9A6'))
        window[(0,5,i)].Update('E',button_color = ('black', '#F3F9A6'))
        window[(0,6,i)].Update('F',button_color = ('black', '#F3F9A6'))
        window[(0,7,i)].Update('G',button_color = ('black', '#F3F9A6'))
        window[(0,8,i)].Update('H',button_color = ('black', '#F3F9A6'))
        window[(0,9,i)].Update('I',button_color = ('black', '#F3F9A6'))
        window[(0,10,i)].Update('J',button_color = ('black', '#F3F9A6'))
    return event, window


#Alix & Laure
#fonction marche parfaitement
def choix_bateau(event, window, etat_mer,compteur_bateaux,bateaux_placer,e):
   
    '''
    Parameters
    ----------
    event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer
    etat_mer : matrice de taille 2*2
        permet de savoir si une case de la mer de l'utilisateur est occupée.
    compteur_bateaux : de type int, entier
        Permet de savoir combien de fois la foncion placement bateau à été appelé (elle compte les bateaux placés). 
    
    Role
    ----
    Cette fonction permet à l'utilisateur de choisir le bateau qu'il veut placer. 
    Une fois choisi cette fonction appelle la fonction placement_bateaux qui
    va lui demander dans quelle direction il veut placer son bateau.

    '''
    for a in range(1,11):
        for b in range(1,11):
            if event==(a,b,1):
                layout_choix=[[sg.Text('Quel bateau voulez-vous placer en premier?')],
                              [sg.Button('porte-avion(5 cases)',key='PA')],
                              [sg.Button('croiseur(4 cases)', key='CR')],
                              [sg.Button('contre-torpilleur1(3 cases)',key='CT')],
                              [sg.Button('contre-torpilleur2(3 cases)',key='CT_2')],
                              [sg.Button('sous-marin(2 cases)', key='SM')],
                              ]
                window_choix = sg.Window('Demande de choix bateau', layout_choix)    
                event_choix, values = window_choix.read()    
                window_choix.close()
                
                
                if event_choix == 'PA':
                    nb = 5
                    if e==1:
                        e=0
                    if bateaux_placer[nb]==0:
                        event,window,etat_mer,compteur_bateaux,bateaux_placer= placement_bateaux(event,window,etat_mer,nb,compteur_bateaux,bateaux_placer,event_choix)
                    else:
                        sg.popup('Vous avez déjà placé le porte avion.')

                if event_choix == 'CR':
                    nb=4
                    if e==1:
                        e=0
                    if bateaux_placer[nb]==0:
                        event,window,etat_mer,compteur_bateaux,bateaux_placer= placement_bateaux(event,window,etat_mer,nb,compteur_bateaux,bateaux_placer,e)
                    else:
                        sg.popup('Vous avez déjà placé le croiseur.')

                if event_choix == 'CT':
                    nb = 3
                    
                    if bateaux_placer[nb]==0:
                        event,window,etat_mer,compteur_bateaux,bateaux_placer= placement_bateaux(event,window,etat_mer,nb,compteur_bateaux,bateaux_placer,e)  
                    else:
                        sg.popup('Vous avez déjà placé le premier contre-torpilleur .')
                
                if event_choix == 'CT_2':
                    nb = 1
                    e=1
                    if bateaux_placer[nb]==0:
                        event,window,etat_mer,compteur_bateaux,bateaux_placer= placement_bateaux(event,window,etat_mer,nb,compteur_bateaux,bateaux_placer,e)
                    else:
                        sg.popup('Vous avez déjà placé le deuxième contre-torpilleur .')
                
                if event_choix == 'SM':
                    nb=2
                    if e==1:
                        e=0
                    if bateaux_placer[nb]==0:
                         event,window,etat_mer,compteur_bateaux,bateaux_placer= placement_bateaux(event,window,etat_mer,nb,compteur_bateaux,bateaux_placer,e)
                         
                    else: 
                        sg.popup('Vous avez déjà placé le sous-marin.')
                    
    return event, window, etat_mer, compteur_bateaux,bateaux_placer,e

#Alix & Laure 
#fonction marche parfaitement      
def placement_bateaux(event,window,etat_mer,nb,compteur_bateaux,bateaux_placer,e):
    """
    Parameters
    ----------
    event : le clique du joueur, de type 'non-type' 
    
    window : la fenêtre qui permet au joueur de jouer
    
    etat_mer : matrice de taille 10*10
        permet de savoir si une case de la mer de l'utilisateur est occupée.
        
    nb : de type int, (entier)
       indice du tableau bateaux_placer
       
    compteur_bateaux : de type int, (entier)
        Permet de savoir combien de fois la foncion placement bateau à été appelé (elle compte les bateaux placés). 
    
    bateaux_placer : tableau contenant 5  0
       dès que la fonction placement_bateaux a été exécuté une fois, on remplace bateaux_placer[nb] par 1 au lieu de 0.
       ce tableau nous permet de vérifier si le bateau de nb case a déjà été placé ou non.
       
    e : de type, int (entier)
        variable qui permet de différncier le premier torpilleur du 2nd

    Returns
    -------
     event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer
    etat_mer : Tmatrice de taille 10*10
        permet de savoir si une case de la mer de l'utilisateur est occupée.
     compteur_bateaux : de type int, (entier)
        Permet de savoir combien de fois la foncion placement bateau à été appelé (elle compte les bateaux placés). 
        
      bateaux_placer : tableau contenant 5  0
       dès que la fonction placement_bateaux a été exécuté une fois, on remplace bateaux_placer[nb] par 1 au lieu de 0.
       ce tableau nous permet de vérifier si le bateau de nb case a déjà été placé ou non.
       
     
    Role
    ----
    
    Placement bateau permet au joueur de choisir la direction de son bateau: Horizontal vers la droite ou vers la gauche ou Vertical vers le haut ou vers le bas.
    """
    if e == 1:
        nb=3
    for a in range(11):
        for b in range(11):
            if event == (a,b,1):
                if etat_mer[a][b] == 'libre':
                    window[(a,b,1)].Update(button_color = ('black'))
                    layout_position =[[sg.Text('Dans quelle direction voulez-vous placer vos bateaux?')],      
                                      [sg.Button('Horizontal/Droite:',key='HD')],
                                      [sg.Button('Horizontal/Gauche:',key='HG')],
                                      [sg.Button('Vertical/Haut:',key='VH')],
                                      [sg.Button('Vertical/Bas:',key='VB')],
                                      [sg.Cancel('Annuler')]
                                      ]      
                    window1 = sg.Window('Demande de placement bateau', layout_position)    
                    event1, values = window1.read()    
                    window1.close()
                    
                    if event1 == 'Annuler':
                        window[(a,b,1)].Update(button_color = ('#009ED9'))
                        etat_mer[a][b] == 'libre'
                        return event, window,etat_mer,compteur_bateaux, bateaux_placer
                    
                    if event1=='HD':
                        if b+nb<=11:
                            for i in range(b,b+nb):
                               if etat_mer[a][i] == 'occupé':
                                   sg.popup("Vous ne pouvez pas superposer vos bateaux")
                                   window[(a,b,1)].Update(button_color = ('#009ED9'))
                                   return event, window,etat_mer,compteur_bateaux, bateaux_placer
                            for j in range(b,b+nb): 
                                window[(a,j,1)].Update(button_color = ('black'))
                                etat_mer[a][j] = 'occupé'
                        else:
                            sg.popup("Il n'y a pas assez de cases disponibles pour ce placement.")
                            window[(a,b,1)].Update(button_color = ('#009ED9'))
                            return event, window,etat_mer,compteur_bateaux, bateaux_placer
                            

                    if event1=='HG':
                        if 0<=b-(nb):
                            for i in range(b-nb+1,b):
                               if etat_mer[a][i] == 'occupé':
                                   sg.popup("Vous ne pouvez pas superposer vos bateaux")
                                   window[(a,b,1)].Update(button_color = ('#009ED9'))
                                   return event, window,etat_mer,compteur_bateaux, bateaux_placer
                            for j in range(b-nb+1,b): 
                                window[(a,j,1)].Update(button_color = ('black'))
                                etat_mer[a][j] = 'occupé'
                        else:
                            sg.popup("Il n'y a pas assez de cases disponibles pour ce placement.")
                            window[(a,b,1)].Update(button_color = ('#009ED9'))
                            return event, window,etat_mer,compteur_bateaux, bateaux_placer


                    if event1=='VH':
                        if 0<=a-(nb):
                            for i in range(a-nb+1,a):
                               if etat_mer[i][b] == 'occupé':
                                   sg.popup("Vous ne pouvez pas superposer vos bateaux")
                                   window[(a,b,1)].Update(button_color = ('#009ED9'))
                                   return event, window,etat_mer,compteur_bateaux, bateaux_placer
                            for j in range(a-nb+1,a): 
                                window[(j,b,1)].Update(button_color = ('black'))
                                etat_mer[j][b] = 'occupé'
                        else:
                            sg.popup("Il n'y a pas assez de cases disponibles pour ce placement.")
                            window[(a,b,1)].Update(button_color = ('#009ED9'))
                            return event, window,etat_mer,compteur_bateaux, bateaux_placer
                        
                        
                    if event1=='VB':
                        if a+nb<=11:
                           for i in range(a,a+nb):
                               if etat_mer[i][b] == 'occupé':
                                   sg.popup("Vous ne pouvez pas superposer vos bateaux")
                                   window[(a,b,1)].Update(button_color = ('#009ED9'))
                                   return event, window,etat_mer,compteur_bateaux, bateaux_placer
                           for j in range(a,a+nb): 
                               window[(j,b,1)].Update(button_color = ('black'))
                               etat_mer[j][b] = 'occupé'
                        else:
                            sg.popup("Il n'y a pas assez de cases disponibles pour ce placement.")
                            window[(a,b,1)].Update(button_color = ('#009ED9'))
                            return event, window,etat_mer,compteur_bateaux, bateaux_placer
                else:
                    sg.popup('Cette case est déjà utilisée','Veuillez recommencer')
                    window[(a,b,1)].Update(button_color = ('#009ED9'))
                    return event, window,etat_mer,compteur_bateaux, bateaux_placer
                    
    bateaux_placer[nb]=1
    compteur_bateaux+=1
    return event, window,etat_mer,compteur_bateaux, bateaux_placer

#Alix&Laure
#fonction marche parfaitement
def placement_ordi(event, window, mer_ordi, bateau, cpt_ordi,nbre):
    '''
    Parameters
    ----------
    event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer
    
    mer_ordi :  matrice 10*10 
    indique si la case est occupée ou libre
    cpt_ordi: compte le nombre de bateau placé par l'ordinateur
    
    bateau : tableau 
        il contient la longueur de chaque bateau 
    nbre : indice du tableau bateau, il va indiquer à l'ordinateur quel bateau placé

    Returns
    -------
    mer_ordi :  matrice 10*10 
        indique si la case est occupée ou libre
    cpt_ordi: de type int, (entier)
        compte le nombre de bateau placé par l'ordinateur
    nbre : du type int, (entier)
        indice du tableau bateau, il va indiquer à l'ordinateur quel bateau placé 
        
    Role
    ----
    
    Cette fonction permet de placer les bateaux de l'ordi aléatoirement sur sa mer.
    Cette dernière ne demande pas l'interaction de l'utilisateur.
    Pour se faire elle choisit aléatoirement une ligne, une colonne et une
    direction dans laquelle elle place le bateaux, cachés de l'utilisateur.
    Elle vérifie que le placement est autorisé puis le place.
    Si le placement est interdit l'ordinateur relance la fonction.
    '''
    n=bateau[nbre]
    #on tire aléatoirement la ligne la colonne et la direction
    ligne = randint(1,10)
    colonne = randint(1,10)
    direction = randint(1,4)
    
    if direction == 1:      #vertical vers le haut
        if 1<=ligne-n:      #condition pour savoir si le placement est autorisé
            for i in range(ligne-n,ligne):
                if mer_ordi[i][colonne] == 'occupé':
                    return mer_ordi,cpt_ordi,nbre
            for j in range(ligne-n,ligne): 
               # window[(j,colonne,0)].Update(button_color = ('black'))
                mer_ordi[j][colonne] = 'occupé'
        else:
            return mer_ordi,cpt_ordi,nbre
        
    if direction ==2:       #vertical vers le bas
        if ligne+n<=11:     #condition pour savoir si le placement est autorisé
            for i in range(ligne,ligne+n): 
                #on teste pour toutes les cases à placer si celle ci sont bien libre
                if mer_ordi[i][colonne] == 'occupé':
                    return mer_ordi,cpt_ordi,nbre #si il y en a une occupée on relance 
            for j in range(ligne,ligne+n): 
                #window[(j,colonne,0)].Update(button_color = ('black'))
                mer_ordi[j][colonne] = 'occupé'
        else: 
            #si le placement n'est pas autorisé on relance la fonction
            return mer_ordi,cpt_ordi,nbre
          
    if direction ==3:       #horizontal vers la droite
        if colonne+n<=10:
            for i in range(colonne,colonne+n):
                if mer_ordi[ligne][i] == 'occupé':
                    return mer_ordi,cpt_ordi,nbre
            for j in range(colonne,colonne+n): 
                #window[(ligne,j,0)].Update(button_color = ('black'))
                mer_ordi[ligne][j] = 'occupé'
        else:
            return mer_ordi,cpt_ordi,nbre
                                           
    if direction == 4:      #horizontal vers la gauche 
        if 1<=colonne-n:
            for i in range(colonne-n,colonne):
                if mer_ordi[ligne][i] == 'occupé':
                    return mer_ordi,cpt_ordi,nbre
            for j in range(colonne-n,colonne): 
               # window[(ligne,j,0)].Update(button_color = ('black'))
                mer_ordi[ligne][j] = 'occupé'
        else:
            return mer_ordi,cpt_ordi,nbre
    
    #si la fonction lit les deux prochaines lignes alors cela veut dire quelles a placer des bateaux
    #on incrémente donc les compteurs    
    nbre +=1     
    cpt_ordi +=1
    return mer_ordi,cpt_ordi,nbre


#Alix&Laure
def tour_ordi(event,window, mer_ordi, etat_mer, score_joueur, score_ordi, tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores):
    '''
    Parameters
    ----------
    event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer
    
    mer_ordi :  matrice 10*10
    indique si la case est occupée ou libre
    etat_mer : matrice de taille 2*2
        permet de savoir si une case de la mer de l'utilisateur est occupée.

    score_ordi : de type int, (entier)
       comptablise le score de l'ordinateur
    score_joueur : de type int, (entier)
       comptablise le score du joueur
       
    tirer : matrice 10*10 
        enregistre les cases où à tirer l'ordinateur
        
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez le joueur 
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez l'ordi

    Returns
    -------
     event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer
    
    mer_ordi :  matrice 10*10 
    indique si la case est occupée ou libre
    etat_mer : matrice de taille 2*2
        permet de savoir si une case de la mer de l'utilisateur est occupée.

    score_ordi : de type int, (entier)
       comptablise le score de l'ordinateur
    score_joueur : de type int, (entier)
       comptablise le score du joueur
       
    tirer : matrice 2*2 
        enregistre les cases où à tirer l'ordinateur
        
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez le joueur 
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez l'ordi
       
     Role
     -----
     Cette fonction permet à l'ordinateur de tirer de manière aléatoire sur la grille du joueur.
     Une fois la case tirée (les coordonnées de la case sont enregistrées afin qu'il ne tire pas 2 fois au même endroit),
     le joueur doit indiquer si la case touche un bateau, en coule un, ou si son tir est raté. 
     le joueur a l'occasion de tricher, si c'est le cas, il perd 10 pts. 

    '''
  
    if score_joueur<=0 or score_ordi<=0 or cpt_fin_de_jeu_joueur==17 or cpt_fin_de_jeu_ordi==17:
        event, window, score_joueur, score_ordi, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores= fin_partie(event, window, score_joueur, score_ordi, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores)
          
        
    x = randint(1,10)
    y = randint(1,10)
    
    if tirer[x][y]==1:
        event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi =tour_ordi(event, window, mer_ordi, etat_mer, score_joueur, score_ordi, tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores)
    if etat_mer[x][y]=='occupé':
        window[(x,y,1)].Update('\u2b24',button_color = ('light blue','black'))
    else:
         window[(x,y,1)].Update('\u2b24',button_color = ('light blue','#009ED9'))
    
    layout_decision =[[sg.Text("Veuillez indiquer si la case touchée par l'ordinateur est touchée, ratée ou coulée:")],      
                          [sg.Button('Touché',key='T')],
                          [sg.Button('Coulé',key='C')],
                          [sg.Button('Raté',key='R')]
                          ]      
    window_decision = sg.Window('Tour ordi', layout_decision)    
    event_decision, values = window_decision.read()    
    window_decision.close()
  
    if event_decision =='R':
        if etat_mer[x][y]=='libre':
            score_ordi -=1
            tirer[x][y] +=1
            window[(x,y,1)].Update('\u2b24',button_color = ('blue','#009ED9'))
            window['scoreJ'].Update(score_joueur)
            window['scoreO'].Update(score_ordi)
            event, window,score_joueur, score_ordi, etat_mer, mer_ordi, tirer,cpt_fin_de_jeu_joueur,cpt_fin_de_jeu_ordi= tour_joueur(event ,window, mer_ordi, etat_mer, score_joueur, score_ordi, tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores)
            #erreur lors de l'appel de la fonction: mer_ordi, etat_mer, score_joueur, score_ordi,
        else:
            sg.popup('Vous avez menti.','Vous perdez 10 points.')
            score_joueur-=10
            window[(x,y,1)].Update('\u2b24',button_color = ('red','black'))
            window['scoreJ'].Update(score_joueur)
            window['scoreO'].Update(score_ordi)
            
    
    if event_decision =='T':
        if etat_mer[x][y]=='occupé':
            cpt_fin_de_jeu_joueur+=1
            print("Bateaux touchés joueur:", cpt_fin_de_jeu_joueur, "\nBateaux touchés ordi:",cpt_fin_de_jeu_ordi)
            print("{:-^70s}".format(""))
            score_ordi +=3
            tirer[x][y] +=1
            window[(x,y,1)].Update('\u2b24',button_color = ('red','black'))
            window['scoreJ'].Update(score_joueur)
            window['scoreO'].Update(score_ordi)
            event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi =tour_ordi(event, window, mer_ordi, etat_mer, score_joueur, score_ordi, tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores)
            
        else:
            sg.popup('Vous avez menti.','Vous perdez 10 points.')
            score_joueur-=10
            window[(x,y,1)].Update('\u2b24',button_color = ('blue','#009ED9'))
            window['scoreJ'].Update(score_joueur)
            window['scoreO'].Update(score_ordi)
            
    
    if event_decision =='C':
        if etat_mer[x][y]=='occupé':
            cpt_fin_de_jeu_joueur+=1
            print("Bateaux touchés joueur:", cpt_fin_de_jeu_joueur, "\nBateaux touchés ordi:",cpt_fin_de_jeu_ordi)
            score_ordi +=3
            tirer[x][y] +=1
            window[(x,y,1)].Update('\u2b24',button_color = ('red','black'))
            window['scoreJ'].Update(score_joueur)
            window['scoreO'].Update(score_ordi)
            event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer,cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi =tour_ordi(event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores)
        
        else:
            sg.popup('Vous avez menti.','Vous perdez 10 points.')
            score_joueur-=10
            window[(x,y,1)].Update('\u2b24',button_color = ('blue','#009ED9'))
            window['scoreJ'].Update(score_joueur)
            window['scoreO'].Update(score_ordi)
                
        
    return event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi


#Alix&Laure
def tour_joueur(event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer,cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores):
    '''
    Parameters
    ----------
    event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer
    mer_ordi :  matrice 10*10
    indique si la case est occupée ou libre
    etat_mer : matrice de taille 2*2
        permet de savoir si une case de la mer de l'utilisateur est occupée.
    score_ordi : de type int, (entier)
    comptablise le score de l'ordinateur
    score_joueur : de type int, (entier)
    comptablise le score du joueur
 
    tirer : matrice 2*2 
        enregistre les cases où à tirer l'ordinateur
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez le joueur 
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez l'ordi

    Returns
    -------
    event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer

    mer_ordi :  matrice 10*10
        indique si la case est occupée ou libre
    etat_mer : matrice de taille 10*10
        permet de savoir si une case de la mer de l'utilisateur est occupée.
        
    score_ordi : de type int, (entier)
       comptablise le score de l'ordinateur
    score_joueur : de type int, (entier)
       comptablise le score du joueur
     
    tirer : matrice 10*10
        enregistre les cases où à tirer l'ordinateur
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez le joueur 
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez l'ordi

    Role
    ----
    Cette fonction permet au joueur de jouer. Il tire sur la grille de l'ordinateur.
    L'ordinateur ne ment jamais. 
    '''   
     
    if score_joueur<=0 or score_ordi<=0 or cpt_fin_de_jeu_joueur==17 or cpt_fin_de_jeu_ordi==17:
        event,window,score_joueur,score_ordi, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores = fin_partie(event,window,score_joueur,score_ordi,cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos,scores) 
    
    event, values = window.read()
    for a in range(0,11):
        for b in range(0,11):
            if event ==(0,b,0) or event==(a,0,0) or event ==(a,b,1):
                event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi= tour_joueur(event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi,pseudos, scores)
            if event == (a,b,0):
                if mer_ordi[a][b]=="occupé":
                    score_joueur +=3
                    window[(a,b,0)].Update('\u2b24',button_color = ('red','black'))
                    cpt_fin_de_jeu_ordi+=1
                    sg.popup('Touché!!','Vous pouvez rejouer!')
                    window['scoreJ'].Update(score_joueur)
                    window['scoreO'].Update(score_ordi)
                    window[(a,b,0)].Update(disabled=True)
                    print("Bateaux touchés joueur:", cpt_fin_de_jeu_joueur, "\nBateaux touchés ordi:",cpt_fin_de_jeu_ordi)
                    print("{:-^70s}".format(""))
                    event, window, mer_ordi, etat_mer, score_joueur, score_ordi, tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi = tour_joueur(event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi,pseudos,scores)
                   
                if mer_ordi[a][b] == 'libre':
                    score_joueur -=1
                    window[(a,b,0)].Update('\u2b24',button_color = ('blue','#009ED9'))
                    sg.popup('Raté!!')
                    window[(a,b,0)].Update(disabled=True)
                    window['scoreJ'].Update(score_joueur)
                    window['scoreO'].Update(score_ordi)
                    event, window, mer_ordi, etat_mer, score_joueur, score_ordi, tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi = tour_ordi(event,window,mer_ordi,etat_mer,score_joueur,score_ordi,tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi,pseudos,scores)
        
    return event, window, mer_ordi, etat_mer, score_joueur, score_ordi, tirer, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi

def fin_partie(event,window,score_joueur,score_ordi,cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi, pseudos, scores):
    """

    Parameters
    ----------
    event : le clique du joueur, de type 'non-type' 
    window : la fenêtre qui permet au joueur de jouer
    score_ordi : de type int, (entier)
    comptablise le score de l'ordinateur
    score_joueur : de type int, (entier)
    comptablise le score du joueur
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez le joueur 
    cpt_fin_de_jeu_joueur : de type int, (entier)
       compte le nombre de case touchée chez l'ordi

    Returns
    -------
    Cette fonction retourne les mêmes variables que celles qu'elle prend en argument.
    ----
    Cette fonction affiche le score à la fin de la partie.

    """
    if cpt_fin_de_jeu_ordi==17 or int(score_ordi)<=0:
        print('Vous avez gagné')
        print("{:-^70s}".format(""))
        print("{:^70s}".format("SCORES"))
        print("{:-^70s}".format(""))
        print("Score joueur:", score_joueur)
        print ("Score ordinateur:",score_ordi)
        print("Vous pouvez quitter la partie.")
        for i in range(11):
            for j in range(11):
                window[(i,j,0)].Update(disabled=True)
                #window[(i,j,1)].Update(disabled=True)
        pseudos_tries, scores_tries =gestion_score(score_joueur, pseudos,scores)
 
    if cpt_fin_de_jeu_joueur==17 or int(score_joueur)<=0:
        print("")
        print("Vous avez perdu!")
        print("{:-^70s}".format(""))
        print("{:^70s}".format("SCORES"))
        print("{:-^70s}".format(""))
        print("Score joueur", score_joueur)
        print ("Score ordinateur:",score_ordi)
        print("Vous pouvez quitter la partie.")
        for i in range(11):
            for j in range(11):
                window[(i,j,0)].Update(disabled=True)
                #☺window[(i,j,1)].Update(disabled=True)
        
    return event,window,score_joueur,score_ordi, cpt_fin_de_jeu_joueur, cpt_fin_de_jeu_ordi,pseudos, scores


def tri_score(pseudos,scores):
    """
    Parameters
    ----------
    pseudos : liste de 100 indices 
        Elle peut contenir jusqu'à 100 pseudos de joueurs différents.
    scores : tableau de 100 indices
        Elle peut contenir jusqu'à 100 scores de joueurs différents.

    Returns
    -------
     pseudos_tri : liste de 100 indices
        La liste des pseudos triés
    scores_tri : tableau de 100 indices
        tableau des scores triés dans l'ordre décroissant
        
    Role
    ----
    Tri le tableau des scores dans l'ordre décroissant.

    """
    for i in range (0,len(scores)-1):
        for j in range (0,len(scores)-1):
            if scores[j+1]>scores[j]:
                temp=scores[j]
                scores[j]=scores[j+1]
                scores[j+1]=temp    
                temp2=pseudos[j]
                pseudos[j]=pseudos[j+1]
                pseudos[j+1]=temp2
    return pseudos, scores
                 
def gestion_score(score_joueur,pseudos, scores):
    """
    Parameters
    ----------
    score_joueur : de type int (entier)
        comptabilise le score du joueur
    pseudos : liste de 100 indices 
        Elle peut contenir jusqu'à 100 pseudos de joueurs différents.
    scores : tableau de 100 indices
        Elle peut contenir jusqu'à 100 scores de joueurs différents 

    Returns
    -------
    pseudos_tri : liste de 100 indices
        La liste des pseudos triés
        DESCRIPTION.
    scores_tri : tableau de 100 indices
        tableau des scores triés dans l'ordre décroissant
        
    Role
    -----
    Cette fonction va permettre au joueur de rentrer son pseudo lorsqu'il gagne. 
    Son score sera associé à son pseudo et affiché dans l'ordre décroissant à l'aide la fonction tri_score.

    """
    layout_score = [[sg.Text('Vous avez gagné bravo! Veuillez entrer votre pseudo.')],
                 [sg.Input(' ', size=(45, 1))],
                 [sg.Button('Valider')]
                 ]
    window_score = sg.Window('Pseudo', layout_score)
    event_score, values = window_score.read()
    pseudo = values
    window_score.close()
    
    if pseudo not in pseudos:
        for i in range (0,99):
            if pseudos[i]=="":
                pseudos[i]=pseudo
                scores[i]=score_joueur
                break
    else:
        for j in range (0,99):
            if pseudos[j]==pseudo:
                scores[j]=scores[j]+score_joueur
    
    pseudos_tri,scores_tri=tri_score(pseudos,scores)            
    for k in range(0,99):
        if scores_tri[k]!=0:  
            print(pseudos_tri[k],':',scores_tri[k])
          
    return pseudos_tri, scores_tri