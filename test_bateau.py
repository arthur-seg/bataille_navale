from bateau import Bateau


def test_init():
    b = Bateau(1, 2)
    assert b.ligne == 1
    assert b.colonne == 2
    assert b.longueur == 1
    assert not b.vertical


def test_positions():
    b = Bateau(2, 3, 3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]
    b = Bateau(2, 3, 3, True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]
