from grille import Grille
from pytest import raises
import re


def test_init():
    g = Grille(1, 2)
    assert g.n_lignes == 1
    assert g.n_colonnes == 2


def test_liste_grille_vide():
    g = Grille(0, 0)
    assert g.liste == []


def test_liste_grille_general():
    g = Grille(2, 3)
    assert g.liste == ["~ ", "~ ", "~ ", "~ ", "~ ", "~ "]


def test_affichage_1(capfd):
    g = Grille(1, 1)
    print(g)
    out, _ = capfd.readouterr()
    assert out == "~ \n"


def test_affichage_colonne(capfd):
    g = Grille(3, 1)
    print(g)
    out, _ = capfd.readouterr()
    assert out == "~ \n~ \n~ \n"


def test_affichage_general(capfd):
    g = Grille(3, 4)
    print(g)
    out, _ = capfd.readouterr()
    assert out == "~ ~ ~ ~ \n~ ~ ~ ~ \n~ ~ ~ ~ \n"


def test_tirer_typeError():
    g = Grille(2, 2)
    with raises(TypeError, match="elle a reçu un str"):
        g.tirer(1, "un")


def test_tirer_valueError():
    g = Grille(2, 3)
    with raises(ValueError, match=re.escape("le tir est hors de la grille (ligne 2 et colonne 2 visées sur une grille à \
2 lignes et 3 colonnes)")):
        g.tirer(2, 2)


def test_tirer():
    g = Grille(2, 3)
    g.tirer(0, 1)
    g.tirer(1, 0)
    g.tirer(1, 2)
    assert g.liste == ["~ ", "x ", "~ ", "x ", "~ ", "x "]


def test_tirer_personalise():
    g = Grille(1, 1)
    g.tirer(0, 0, "o")
    assert g.liste == ["o"]
