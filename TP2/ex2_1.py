def pgcd_naif(a,b):
    pgcd = 1;
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            pgcd = i
    print(pgcd)

print("PGCD Naïf")
pgcd_naif(28,16)
pgcd_naif(14,7)

def pgcd(a,b):
    pgcd = 1;
    aModb = a % b
    for i in range(1, min(a,b)+1):
        if b % i == 0 and aModb % i == 0:
            pgcd = i
    print(pgcd)

print("PGCD (Euclide)")
pgcd(28,16)
pgcd(14,7)