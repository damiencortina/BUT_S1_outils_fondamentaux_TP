from functions import evaluer
import timeit

print(evaluer([2, 3, 0, 5], 2))
print(evaluer([2, 3, 0, 5], 0))

coeffs = range(10001)

t_a = timeit.timeit("evaluer(coeffs, 2)","from __main__ import evaluer, coeffs", number=100)

print(f"Evaluer (Schéma d'Horner) : {t_a:.10f} s ")

# Sur un polynöme de degré 10000, l'évaluation est environ 20 fois plus rapide avec le Shéma d'Horner
