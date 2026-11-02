def nombre_de_chiffres(n):
    longueur = 0
    while n > 0:
        n //= 10
        longueur += 1
    return longueur

print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))