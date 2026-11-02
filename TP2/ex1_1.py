def diviseurs(a):
    divs = [];
    for i in range(1, a+1):
        if a % i == 0:
            divs.append(i)
    print(divs)

diviseurs(28)


def est_parfait(n):
    return sum(d for d in range(1, n) if n % d == 0) == n

print([n for n in range(2, 10000) if est_parfait(n)])