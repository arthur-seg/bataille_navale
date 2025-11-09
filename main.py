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


### fonctions ###
def jeu_est_fini(grille):
    for bateau in grille.bateaux_ajoutes:
        if bateau.coule(grille) is False:
            return False
    return True


print("---------------BATAILLE NAVALE---------------")
reponse = input("appuyer sur s pour commencer ou q pour quitter\n")
if reponse != 's':
    quit()
while 1:
    # init le jeu
    nombre_coups = 0
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
    grille_utilisateur = Grille(n_lignes_grille, n_colonnes_grille)  # grille affichée à l'utilisateur
    # boucle de gameplay jusqu'a la fin
    jeu_fini = False
    while not jeu_fini:
        print(grille_utilisateur)
        result = None
        ligne_tir = -1
        colonne_tir = -1
        while result is None or ligne_tir < 0 or ligne_tir >= n_lignes_grille or \
                colonne_tir < 0 or colonne_tir >= n_colonnes_grille:
            tir_utilisateur = input("où tirer, capitaine ?\nentrez la ligne puis la colonne\n")
            if tir_utilisateur == 'q':
                quit()
            pattern = re.compile("\(?(\d+)[ ,;]+(\d+)\)?")
            result = pattern.fullmatch(tir_utilisateur)
            if result is None:
                print("coordonnées incompréhensibles. Réessayez.")
            else:
                ligne_tir = int(result.group(1))
                colonne_tir = int(result.group(2))
                if ligne_tir < 0 or ligne_tir >= n_lignes_grille or colonne_tir < 0 or colonne_tir >= n_colonnes_grille:
                    print("ce tir est hors de la grille !")
        nombre_coups += 1
        grille.tirer(ligne_tir, colonne_tir)
        grille_utilisateur.tirer(ligne_tir, colonne_tir)
        touche = False
        for bateau in grille.bateaux_ajoutes:
            for position in bateau.positions:
                if (ligne_tir, colonne_tir) == position:
                    touche = True
                    grille_utilisateur.tirer(ligne_tir, colonne_tir, '💣')
                    if bateau.coule(grille):
                        print("bateau adverse coulé !")
                        grille_utilisateur.ajoute(bateau)
                        jeu_fini = jeu_est_fini(grille)
                    break
                if touche:
                    break
    # demander une nouvelle partie
    print(grille_utilisateur)
    print("bravo ! vous avez détruit la flotte adverse en {} coups !".format(nombre_coups))
    while reponse != 'o' and reponse != 'n':
        reponse = input("prêt pour une nouvelle partie ? (o ou n)\n")
        if reponse != 'o' and reponse != 'n' and reponse != 'q':
            print("je n'ai pas compris votre réponse")
        elif reponse == 'o':
            print("c'est reparti !")
        else:
            quit()
