from grille import Grille
import bateau as bat
from positionutils import PositionsPossibles
from random import random, shuffle
import re


### constantes ###
n_lignes_grille = 8
n_colonnes_grille = 10
dict_bateaux = {"porte-avion": bat.PorteAvion, "croiseur": bat.Croiseur,
                "torpilleur": bat.Torpilleur, "sous-marin": bat.SousMarin}
echec_ajout = 1
succes_ajout = 0


print("---------------BATAILLE NAVALE---------------")
reponse = input("appuyer sur s pour commencer ou q pour quitter\n")
if reponse != 's':
    quit()
while reponse != 'q':
    # init le jeu
    len_liste_grille = n_colonnes_grille * n_lignes_grille
    grille = Grille(n_lignes_grille, n_colonnes_grille)
    positions_possibles = PositionsPossibles(grille, list(dict_bateaux.values()))
    # placer les bateaux
    bateaux = list(dict_bateaux.values())
    shuffle(bateaux)
    while len(bateaux) > 0:
        bateau = bateaux.pop()(0, 0, (random() > 0.5))
        pos = positions_possibles.get_position_for(bateau)
        bateau.ligne = pos // n_colonnes_grille
        bateau.colonne = pos % n_colonnes_grille
        grille.ajoute(bateau)
    # boucle de gameplay jusqu'a la fin
    grille_utilisateur = Grille(n_lignes_grille, n_colonnes_grille) # grille affichée à l'utilisateur
    print(grille_utilisateur)
    result = None
    idx_tir = -1
    while result is None or idx_tir < 0 or idx_tir >= len_liste_grille:
        tir_utilisateur = input("où tirer, capitaine ?\nentrez la ligne puis la colonne\n")
        if tir_utilisateur == 'q':
            quit()
        pattern = re.compile("\(?(\d+)[ ,;]+(\d+)\)?")
        result = pattern.fullmatch(tir_utilisateur)
        if result is None:
            print("coordonnées incompréhensibles. Réessayez.")
        else:
            ligne_tir = result.group(1)
            colonne_tir = result.group(2)
            idx_tir = ligne_tir * n_colonnes_grille + colonne_tir
            if idx_tir >= len_liste_grille:
                print("ce tir est hors de la grille !")
    # demander une nouvelle partie
    reponse = input("?\n")    #### PAS ENLEVER
