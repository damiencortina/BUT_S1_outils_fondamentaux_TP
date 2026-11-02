from functions import dichotomie

def test_func(x):
    return x**2-2

print(dichotomie(test_func, 0, 2, 1e-2))

