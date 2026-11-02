from functions import duree, est_premier

def est_premier_naif(n):
    """Teste la primalité en essayant tous les diviseurs jusqu'à n - 1."""
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

print(est_premier_naif(97), est_premier_naif(91))

print(est_premier(97), est_premier(91), est_premier(2), est_premier(1))

n = 1_000_003  # un nombre premier
print(f"naif        : {duree(est_premier_naif, n):.4f} s")
print(f"jusqu'a rac : {duree(est_premier, n):.6f} s")

for n in (10_007, 100_003, 1_000_003):
    t_naif = duree(est_premier_naif, n)
    t_rac = duree(est_premier, n)
    print(f"{n:>9} : naif {t_naif:.5f} s | racine {t_rac:.6f} s")

# Quand n est multiplié par 10, le temps d'éxecution naif l'est aussi, mais ce n'est pas le cas pour la méthode s'arrètant à la racine.