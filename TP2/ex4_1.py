import time

from functions import est_premier, crible

premiers = crible(100)
print(premiers)
print(len(premiers), "premiers jusqu'a 100")

debut = time.perf_counter()
pcrible = len(crible(100_000))
t_crible = time.perf_counter() - debut

debut = time.perf_counter()
psimple = sum(1 for n in range(100_001) if est_premier(n))
t_un_par_un = time.perf_counter() - debut

print(pcrible, psimple)
print(f"crible {t_crible:.4f} s | un par un {t_un_par_un:.4f} s")
