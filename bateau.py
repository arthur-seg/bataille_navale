class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self._icone = '⛵'

    @property
    def icone(self):
        return self._icone

    @icone.setter
    def icone(self, new):
        raise AttributeError("l'attribut 'icone' de la classe Bateau ne peut pas être modifié")

    @property
    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def coule(self, grille):
        try:
            if self not in grille.bateaux_ajoutes:
                raise ValueError("ce bateau n'a pas été ajouté à cette grille")
            else:
                for pos in self.positions:
                    if grille.liste[pos[1] + grille.n_colonnes * pos[0]] == self._icone:
                        return False
                return True
        except AttributeError:
            raise TypeError("la méthode coule() n'accepte que des instances de la classe Grille mais \
elle a reçu un {}".format(type(grille).__name__))


class PorteAvion(Bateau):
    longueur = 4

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)
        self._icone = '🚢'


class SousMarin(Bateau):
    longueur = 2

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self._icone = '🐟'


class Croiseur(Bateau):
    longueur = 3

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)
        self._icone = '⛴'


class Torpilleur(Bateau):
    longueur = 2

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self._icone = '🚣'
