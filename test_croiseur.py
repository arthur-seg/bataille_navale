from croiseur import Croiseur
from grille import Grille
from pytest import raises


def test_init():
    p = Croiseur(2, 3)
    assert p.ligne == 2
    assert p.colonne == 3
    assert p.longueur == 3
    assert not p.vertical
    assert p.icone == '⛴'


def test_icone_setter():
    p = Croiseur(0, 0)
    with raises(AttributeError, match="l'attribut 'icone'"):
        p.icone = "croiseur"


def test_ajoute_croiseur():
    g = Grille(2, 5)
    p = Croiseur(1, 1)
    g.ajoute(p)
    assert g.liste == ["~", "~",     "~",     "~",     "~",
                       "~", p.icone, p.icone, p.icone, "~"]
