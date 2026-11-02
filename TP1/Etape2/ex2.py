def presque_egaux(a, b):
    return abs(a - b) < 1e-10

print("0.1 + 0.2 == 0.3 : " + str(0.1 + 0.2 == 0.3))
print("presque_egaux(0.1 + 0.2, 0.3) : " + str(presque_egaux(0.1 + 0.2, 0.3)))
