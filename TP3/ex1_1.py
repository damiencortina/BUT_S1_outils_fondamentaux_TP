from functions import evaluer_naif
import timeit

print(evaluer_naif([2, 3, 0, 5], 2))
print(evaluer_naif([2, 3, 0, 5], 0))

coeffs = range(10000)

t_a = timeit.timeit("evaluer_naif(coeffs, 2)","from __main__ import evaluer_naif, coeffs", number=100)

print(f"Evaluer Naïf : {t_a:.10f} s ")