from grille import Grille
import bateau as bat
from positionutils import PositionsPossibles
from random import random, shuffle


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
    print(grille)
    # demander une nouvelle partie
    reponse = input("?\n")    #### PAS ENLEVER
