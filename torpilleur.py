from bateau import Bateau


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self._icone = '🚣'
