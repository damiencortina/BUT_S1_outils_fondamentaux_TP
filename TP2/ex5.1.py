import math

from functions import crible


def facteurs(n):
    prime_factors = []
    primes_numbers_to_test = crible(math.floor(math.sqrt(n)))
    tested_prime_number_index = 0
    while n != 1:
        if n % primes_numbers_to_test[tested_prime_number_index] == 0:
            prime_factors.append(primes_numbers_to_test[tested_prime_number_index])
            n //= primes_numbers_to_test[tested_prime_number_index]
        else:
            if tested_prime_number_index < len(primes_numbers_to_test) - 1:
                tested_prime_number_index += 1
            else:
                prime_factors.append(n)
                n = 1
    return prime_factors


print(facteurs(100))
print(facteurs(12))
print(facteurs(54))
print(facteurs(17))
print(facteurs(34))
