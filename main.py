from grille import Grille
import bateau as bat
from random import randrange, shuffle


### constantes ###
n_lignes_grille = 8
n_colonnes_grille = 10
dict_bateaux = {"porte-avion": bat.PorteAvion(0, 0), "croiseur": bat.Croiseur(0, 0),
                "torpilleur": bat.Torpilleur(0, 0), "sous-marin": bat.SousMarin(0, 0)}
echec_ajout = 1
succes_ajout = 0


print("---------------BATAILLE NAVALE---------------")
reponse = input("appuyer sur s pour commencer ou q pour quitter\n")
if reponse != 's':
    quit()
while reponse != 'q':
    # init le jeu
    len_liste_grille = n_colonnes_grille * n_lignes_grille
    positions_possibles_porte_avion_vertical = set(range(len_liste_grille))
    for i in range(len_liste_grille):
        if i // n_colonnes_grille > n_lignes_grille - dict_bateaux["porte-avion"].longueur:
            positions_possibles_porte_avion_vertical.discard(i)

    positions_possibles_porte_avion_horizontal = set(range(len_liste_grille))
    for i in range(len_liste_grille):
        if i % n_colonnes_grille > n_colonnes_grille - dict_bateaux["porte-avion"].longueur:
            positions_possibles_porte_avion_horizontal.discard(i)

    positions_possibles_croiseur_vertical = set(range(len_liste_grille))
    for i in range(len_liste_grille):
        if i // n_colonnes_grille > n_lignes_grille - dict_bateaux["croiseur"].longueur:
            positions_possibles_croiseur_vertical.discard(i)

    positions_possibles_croiseur_horizontal = set(range(len_liste_grille))
    for i in range(len_liste_grille):
        if i % n_colonnes_grille > n_colonnes_grille - dict_bateaux["croiseur"].longueur:
            positions_possibles_croiseur_horizontal.discard(i)

    positions_possibles_torpilleur_vertical = set(range(len_liste_grille))
    for i in range(len_liste_grille):
        if i // n_colonnes_grille > n_lignes_grille - dict_bateaux["torpilleur"].longueur:
            positions_possibles_torpilleur_vertical.discard(i)

    positions_possibles_torpilleur_horizontal = set(range(len_liste_grille))
    for i in range(len_liste_grille):
        if i % n_colonnes_grille > n_colonnes_grille - dict_bateaux["torpilleur"].longueur:
            positions_possibles_torpilleur_horizontal.discard(i)

    positions_possibles_sous_marin_vertical = set(range(len_liste_grille))
    for i in range(len_liste_grille):
        if i // n_colonnes_grille > n_lignes_grille - dict_bateaux["sous-marin"].longueur:
            positions_possibles_sous_marin_vertical.discard(i)

    positions_possibles_sous_marin_horizontal = set(range(len_liste_grille))
    for i in range(len_liste_grille):
        if i % n_colonnes_grille > n_colonnes_grille - dict_bateaux["sous-marin"].longueur:
            positions_possibles_sous_marin_horizontal.discard(i)
    # placer les bateaux
    # boucle de gameplay jusqu'a la fin
    # demander une nouvelle partie
    t = [False for _ in range(len_liste_grille)]
    for i in positions_possibles_sous_marin_vertical:
        t[i] = True
    for i, elt in enumerate(t):
        if i % n_colonnes_grille == 0:
            print('')
        print(elt, end=('  ' if elt is True else ' '))
    reponse = input("?\n")    #### PAS ENLEVER
