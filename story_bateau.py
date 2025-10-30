from bateau import Bateau

# situation 1 : deux bateaux qui ne se chevauchent pas
b1 = Bateau(0, 0, 3, True)
b2 = Bateau(0, 1, 3)
for pos1 in b1.positions:
    for pos2 in b2.positions:
        try:
            assert pos1 != pos2
        except AssertionError:
            print("ca touche...")
print("tout va bien")

# situation 2 deux bateaux qui se chevauchent
b2 = Bateau(1, 0, 3)
for pos1 in b1.positions:
    for pos2 in b2.positions:
        try:
            assert pos1 != pos2
        except AssertionError:
            print("ca touche (donc tout va bien)")
