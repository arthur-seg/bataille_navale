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
