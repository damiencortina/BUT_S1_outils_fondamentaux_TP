import math


def heron(a, tolerance=1e-12):
    if a < 0:
        raise ValueError("a must be positive")
    if a == 0:
        return 0
    found = False
    xn = a / 2
    turns = 0
    while not found:
        xn1 = (xn + a / xn) / 2
        if abs(xn - xn1) < tolerance:
            found = True
        xn = xn1
        turns += 1
    return xn, turns


sqrt2 = math.sqrt(2)
heron2 = heron(2)

print(sqrt2)
print(str(heron2[0]) + " turns: " + str(heron2[1]))
print(abs(sqrt2 - heron2[0]))

heron1e6 = heron(1e6)
print(str(heron1e6[0]) + " turns: " + str(heron1e6[1]))
heron1e20 = heron(1e20)
print(str(heron1e20[0]) + " turns: " + str(heron1e20[1]))
