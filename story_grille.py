from grille import Grille


# on creé une grille 5x8 puis on l'affiche
g = Grille(5, 8)
print(g)

# on demande à l'utilisateur de saisir une ligne et une colonne et on tire à cet endroit
while 1:
    x = input("saisir une ligne\n")
    if x == 'q':
        break
    y = input("saisir une colonne\n")
    if y == 'q':
        break
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("saisie invalide (il faut des entiers)")
    try:
        g.tirer(x, y)
        print(g)
    except ValueError:
        print("le tir est hors-jeu!")
