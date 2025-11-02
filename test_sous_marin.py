from sous_marin import SousMarin
from grille import Grille
from pytest import raises


def test_init():
    p = SousMarin(2, 3)
    assert p.ligne == 2
    assert p.colonne == 3
    assert p.longueur == 2
    assert not p.vertical
    assert p.icone == '🐟'


def test_icone_setter():
    p = SousMarin(0, 0)
    with raises(AttributeError, match="l'attribut 'icone'"):
        p.icone = "sous-marin"


def test_ajoute_sous_marin():
    g = Grille(2, 5)
    p = SousMarin(1, 1)
    g.ajoute(p)
    assert g.liste == ["~", "~",     "~",     "~",     "~",
                       "~", p.icone, p.icone, "~",     "~"]
