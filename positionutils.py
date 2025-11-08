from random import choice


BATEAU_HORIZONTAL = 0
BATEAU_VERTICAL = 1


class PositionsPossibles():
    """Pour chacun des types de bateaux spécifiés, crée un set de ces positions sur
    la grille qui garantissent l'absence de recouvrement et de dépassement.
    Met à jour ces positions lorsqu'une position est récupérée pour un type
    de bateau donné."""
    def __init__(self, grille, types_bateaux):
        self.grille = grille
        self.len_liste_grille = len(self.grille.liste)
        self.types_bateaux = types_bateaux
        # chaque type est associé à deux sets : un pour l'état vertical, un pour l'état horizontal
        self.positions_possibles = {type_bateau: [set(range(self.len_liste_grille)) for _ in range(2)]
                                    for type_bateau in types_bateaux}
        self.init_positions_possibles()

    def init_positions_possibles(self):
        for type_bateau in self.types_bateaux:
            for i in range(self.len_liste_grille):
                if i % self.grille.n_colonnes > self.grille.n_colonnes - type_bateau.longueur:
                    self.positions_possibles[type_bateau][BATEAU_HORIZONTAL].discard(i)
                if i // self.grille.n_colonnes > self.grille.n_lignes - type_bateau.longueur:
                    self.positions_possibles[type_bateau][BATEAU_VERTICAL].discard(i)

    def get_position_for(self, bateau):
        """Renvoie une position aléatoire pour le bateau spécifié. Met à jour les posisions possibles."""
        coordonnees = choice(list(self.positions_possibles[type(bateau)][bateau.vertical]))
        bateau.ligne = coordonnees // self.grille.n_colonnes
        bateau.colonne = coordonnees % self.grille.n_colonnes
        for position in bateau.positions:
            for type_bateau in self.types_bateaux:
                for i in range(type_bateau.longueur):
                    self.positions_possibles[type_bateau][BATEAU_HORIZONTAL].discard(
                        position[0] * self.grille.n_colonnes + position[1] - i)
                    self.positions_possibles[type_bateau][BATEAU_VERTICAL].discard(
                        (position[0] - i) * self.grille.n_colonnes + position[1])
        return coordonnees
