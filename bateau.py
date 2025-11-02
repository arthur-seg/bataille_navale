class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self._icone = '⛵'
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

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
