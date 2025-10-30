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


def test_affiche_1(capfd):
    g = Grille(1, 1)
    g.affiche()
    out, _ = capfd.readouterr()
    assert out == "~\n"


def test_affiche_colonne(capfd):
    g = Grille(3, 1)
    g.affiche()
    out, _ = capfd.readouterr()
    assert out == "~\n~\n~\n"


def test_affiche_general(capfd):
    g = Grille(3, 4)
    g.affiche()
    out, _ = capfd.readouterr()
    assert out == "~~~~\n~~~~\n~~~~\n"
