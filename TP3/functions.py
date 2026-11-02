import time

def duree(fonction, arguments):
    debut = time.perf_counter()
    result = fonction(*arguments)
    return result, time.perf_counter() - debut

def compare(fonction1, fonction2, args):
    result1, t1 = duree(fonction1, args)
    result2, t2 = duree(fonction2, args)
    print(f"Comparaison entre {fonction1.__name__} et {fonction2.__name__}")
    print(f"{fonction1.__name__} : {result1} ({t1:.5f} s)")
    print(f"{fonction2.__name__} : {result2} ({t2:.5f} s)")
    if t1 < t2:
        print(f"{fonction1.__name__} {t2 / t1:.1f} plus rapide")
    else:
        print(f"{fonction2.__name__} {t1 / t2:.1f} plus rapide")
    if result1 == result2:
        print("résultats identiques")
    else:
        print(f"ecart des valeurs :{abs(result1 - result2):.2e}")
    print("--------------------")

def evaluer_naif(P, x):
    total = 0
    for i in range(len(P)):
        total = total + P[i] * x ** i
    return total

def evaluer(P, x):
    total = 0
    for coeff in reversed(P):
         total = total * x + coeff
    return total

def deriver(P):
    return [(i+1) * coeff for i, coeff in enumerate(P[1:])]

def dichotomie(f, a, b, tolerance):
    if a > b:
        temp = a
        a = b
        b = temp
    fa = f(a)
    fb = f(b)
    if fb == 0:
        return fb
    if fa == 0:
        return fa
    x = b - a
    fx = f(x)
    while abs(fx) > tolerance :
        x = (b + a) / 2
        fx = f(x)
        if  fa*fx > 0:
            a = x
            fa = f(a)
        else:
            b = x
    return x

def newton(P, depart, tolerance):
    fx = evaluer(P, depart)
    count = 0
    while abs(fx) > tolerance:
        print(depart)
        depart = depart  - fx / evaluer(deriver(P), depart)
        fx = evaluer(P, depart)
        count+=1
    print(f"nombre d'itérations : {count}")
    return depart