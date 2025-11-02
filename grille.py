from bateau import Bateau


class Grille:
    def __init__(self, n_lignes, n_colonnes):
        self.n_lignes = n_lignes
        self.n_colonnes = n_colonnes
        self.vide = "~"
        self.tir = "x"
        self.liste = [self.vide for _ in range(n_lignes*n_colonnes)]

    def __str__(self):
        string = ""
        for idx, elt in enumerate(self.liste):
            if idx % self.n_colonnes == 0 and idx != 0:
                string += '\n'
            string += elt
        return string

    def tirer(self, ligne, colonne):
        try:
            assert isinstance(ligne, int)
            assert isinstance(colonne, int)
        except AssertionError:
            raise TypeError("la methode tirer() accepte seulement les entiers mais \
elle a recu un {}".format(type(ligne).__name__ if not isinstance(ligne, int) else type(colonne).__name__))
        try:
            assert ligne >= 0
            assert colonne >= 0
            assert ligne < self.n_lignes
            assert colonne < self.n_colonnes
        except AssertionError:
            raise ValueError("le tir est hors de la grille (ligne {} et colonne {} visées sur une grille à \
{} lignes et {} colonnes)".format(ligne, colonne, self.n_lignes, self.n_colonnes))
        self.liste[colonne + ligne * self.n_colonnes] = self.tir

    def ajoute(self, bateau):
        if not isinstance(bateau, Bateau):
            raise TypeError("la méthode ajoute() n'accepte que des instances de la classe Bateau mais elle \
a recu un {}".format(type(bateau).__name__))
        else:
            liste_temp = self.liste.copy()
            for pos in bateau.positions:
                if pos[0] < 0 or pos[0] >= self.n_lignes or pos[1] < 0 or pos[1] >= self.n_colonnes\
                   or liste_temp[pos[1] + pos[0] * self.n_colonnes] == bateau.icone:
                    break
                liste_temp[pos[1] + pos[0] * self.n_colonnes] = bateau.icone
            self.liste = liste_temp
