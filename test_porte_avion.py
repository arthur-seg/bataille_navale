from porte_avion import PorteAvion
from grille import Grille
from pytest import raises


def test_init():
    p = PorteAvion(2, 3)
    assert p.ligne == 2
    assert p.colonne == 3
    assert p.longueur == 4
    assert not p.vertical
    assert p.icone == '🚢'


def test_icone_setter():
    p = PorteAvion(0, 0)
    with raises(AttributeError, match="l'attribut 'icone'"):
        p.icone = "porte_avion"


def test_ajoute_porte_avion():
    g = Grille(2, 5)
    p = PorteAvion(1, 1)
    g.ajoute(p)
    assert g.liste == ["~", "~",     "~",     "~",     "~",
                       "~", p.icone, p.icone, p.icone, p.icone]
