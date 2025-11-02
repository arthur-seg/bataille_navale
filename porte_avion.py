from bateau import Bateau


class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)
        self._icone = '🚢'
