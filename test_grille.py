from grille import Grille


def test_init():
    g = Grille(1, 2)
    assert g.n_lignes == 1
    assert g.n_colonnes == 2


def test_liste_grille_vide():
    g = Grille(0, 0)
    assert g.liste == []


def test_liste_grille_general():
    g = Grille(2, 3)
    assert g.liste == ["~", "~", "~", "~", "~", "~"]
