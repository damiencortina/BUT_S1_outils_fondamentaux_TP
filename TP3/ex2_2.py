from functions import evaluer_naif, evaluer, compare

for degre in (1000, 5000, 20000):
    P = [1] * (degre + 1)
    compare(evaluer, evaluer_naif, [P, 1.0001])

# On constate que la horner est bien environ 2 fois plus rapide que evaluer_naif
# Mes résultats divergent pour le degré 20000, selon mois cela est dû a la manipulation des floats (perte de précision quand les nombre grandissent trop, les deux algos ayant des méthodes de calcul différentes, la précision n'est pas perdue au même moment)

# Comparaison entre evaluer et evaluer_naif
# evaluer : 1052.7590914249245 (0.00003 s)
# evaluer_naif : 1052.7590914249245 (0.00005 s)
# evaluer 1.7 plus rapide
# résultats identiques
# --------------------
# Comparaison entre evaluer et evaluer_naif
# evaluer : 6488.44923936749 (0.00011 s)
# evaluer_naif : 6488.44923936749 (0.00022 s)
# evaluer 2.0 plus rapide
# résultats identiques
# --------------------
# Comparaison entre evaluer et evaluer_naif
# evaluer : 63890.56111243616 (0.00043 s)
# evaluer_naif : 63890.56111243617 (0.00087 s)
# evaluer 2.0 plus rapide
# ecart des valeurs :7.28e-12
# --------------------
