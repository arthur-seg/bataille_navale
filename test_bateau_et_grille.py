from bateau import Bateau
from grille import Grille
from pytest import raises


def test_ajoute_typeError():
    g = Grille(5, 8)
    with raises(TypeError, match="elle a reçu un str"):
        g.ajoute("bateau")
    assert g.bateaux_ajoutes == []


def test_ajoute_hors_jeu():
    g = Grille(5, 8)
    b = Bateau(5, 2, 3)
    g.ajoute(b)
    assert g.bateaux_ajoutes == []
    assert g.liste == ["~" for _ in range(g.n_lignes * g.n_colonnes)]


def test_ajoute_general():
    g = Grille(5, 5)
    b = Bateau(2, 2, 2)
    g.ajoute(b)
    assert g.liste == ["~", "~", "~", "~", "~",
                       "~", "~", "~", "~", "~",
                       "~", "~", b.icone, b.icone, "~",
                       "~", "~", "~", "~", "~",
                       "~", "~", "~", "~", "~"]
    assert g.bateaux_ajoutes == [b]


def test_ajoute_chevauchement():
    g = Grille(3, 3)
    b1 = Bateau(0, 0, 2, True)
    b2 = Bateau(1, 0, 2)
    g.ajoute(b1)
    g.ajoute(b2)
    assert g.liste == [b1.icone, "~", "~",
                       b1.icone, "~", "~",
                       "~",       "~", "~"]
    assert g.bateaux_ajoutes == [b1]


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
    assert g.bateaux_ajoutes == [b1, b2, b3, b4]


def test_coule_typeError():
    b = Bateau(0, 0)
    with raises(TypeError, match="elle a reçu un int"):
        b.coule(1)


def test_coule_bateau_pas_ajoute():
    b = Bateau(0, 0)
    g = Grille(1, 1)
    with raises(ValueError, match="ce bateau n'a pas été ajouté"):
        b.coule(g)


def test_coule_bateau_pas_coule():
    b = Bateau(0, 0, 3)
    g = Grille(3, 3)
    g.ajoute(b)
    g.tirer(0, 0)
    g.tirer(0, 1, 'o')
    assert not b.coule(g)


def test_coule_bateau_coule():
    b = Bateau(0, 0, 3)
    g = Grille(3, 3)
    g.ajoute(b)
    g.tirer(0, 0)
    g.tirer(0, 1, 'o')
    g.tirer(0, 2)
    assert b.coule(g)
