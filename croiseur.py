from bateau import Bateau


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)
        self._icone = '⛴'
