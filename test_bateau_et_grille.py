from bateau import Bateau
from grille import Grille
from pytest import raises


def test_ajoute_typeError():
    g = Grille(5, 8)
    with raises(TypeError, match="elle a recu un str"):
        g.ajoute("bateau")


def test_ajoute_hors_jeu():
    g = Grille(5, 8)
    b = Bateau(5, 2, 3)
    g.ajoute(b)
    assert g.liste == ["~" for _ in range(g.n_lignes * g.n_colonnes)]


def test_ajoute_chevauchement():
    g = Grille(3, 3)
    b1 = Bateau(0, 0, 2, True)
    b2 = Bateau(1, 0, 2)
    g.ajoute(b1)
    g.ajoute(b2)
    assert g.liste == [b1.icone, "~", "~",
                       b1.icone, "~", "~",
                       "~",       "~", "~"]


def test_ajoute_general():
    g = Grille(5, 5)
    b = Bateau(2, 2, 2)
    g.ajoute(b)
    assert g.liste == ["~", "~", "~", "~", "~",
                       "~", "~", "~", "~", "~",
                       "~", "~", b.icone, b.icone, "~",
                       "~", "~", "~", "~", "~",
                       "~", "~", "~", "~", "~"]


def test_ajoute_limite():
    g = Grille(5, 5)
    b1 = Bateau(0, 0, 5)
    b2 = Bateau(1, 0, 4, True)
    b3 = Bateau(4, 1, 4)
    b4 = Bateau(1, 4, 3, True)
    g.ajoute(b1)
    g.ajoute(b2)
    g.ajoute(b3)
    g.ajoute(b4)
    assert g.liste == [b1.icone, b1.icone, b1.icone, b1.icone, b1.icone,
                       b1.icone,    "~",     "~",      "~",    b1.icone,
                       b1.icone,    "~",     "~",      "~",    b1.icone,
                       b1.icone,    "~",     "~",      "~",    b1.icone,
                       b1.icone, b1.icone, b1.icone, b1.icone, b1.icone]
