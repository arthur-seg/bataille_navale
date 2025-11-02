from bateau import Torpilleur
from grille import Grille
from pytest import raises


def test_init():
    p = Torpilleur(2, 3)
    assert p.ligne == 2
    assert p.colonne == 3
    assert p.longueur == 2
    assert not p.vertical
    assert p.icone == '🚣'


def test_icone_setter():
    p = Torpilleur(0, 0)
    with raises(AttributeError, match="l'attribut 'icone'"):
        p.icone = "torpilleur"


def test_ajoute_torpilleur():
    g = Grille(2, 5)
    p = Torpilleur(1, 1)
    g.ajoute(p)
    assert g.liste == ["~", "~",     "~",     "~",     "~",
                       "~", p.icone, p.icone, "~", "~"]
