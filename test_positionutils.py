from positionutils import PositionsPossibles
import bateau
from grille import Grille


def test_init():
    BATEAU_HORIZONTAL = 0
    BATEAU_VERTICAL = 1
    g = Grille(4, 4)
    types_bateaux = [bateau.PorteAvion, bateau.Croiseur, bateau.Torpilleur]
    pp = PositionsPossibles(g, types_bateaux)
    assert pp.positions_possibles[bateau.PorteAvion][BATEAU_HORIZONTAL] == {0, 4, 8, 12}
    assert pp.positions_possibles[bateau.PorteAvion][BATEAU_VERTICAL] == {0, 1, 2, 3}
    assert pp.positions_possibles[bateau.Croiseur][BATEAU_HORIZONTAL] == {0, 1, 4, 5, 8, 9, 12, 13}
    assert pp.positions_possibles[bateau.Croiseur][BATEAU_VERTICAL] == {0, 1, 2, 3, 4, 5, 6, 7}
    assert pp.positions_possibles[bateau.Torpilleur][BATEAU_HORIZONTAL] == {0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14}
    assert pp.positions_possibles[bateau.Torpilleur][BATEAU_VERTICAL] == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}


def test_get_position_for():
    BATEAU_HORIZONTAL = 0
    BATEAU_VERTICAL = 1
    g = Grille(3, 4)
    b = bateau.Torpilleur(1, 2)
    types_bateaux = [bateau.PorteAvion, bateau.Croiseur, bateau.Torpilleur]
    pp = PositionsPossibles(g, types_bateaux)
    pos = pp.get_position_for(b)
    for type_bateau in types_bateaux:
        assert pos - 1 not in pp.positions_possibles[type_bateau][BATEAU_HORIZONTAL]
        assert pos - g.n_colonnes not in pp.positions_possibles[type_bateau][BATEAU_VERTICAL]
