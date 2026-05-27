import math
import random


def miller_rabin(n: int) -> bool:
    if n == 2 or n == 3:
        return True

    if n == 1 or n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    k = int(math.log2(n))
    for i in range(k):
        witness = random.randint(2, n - 2)

        # Modular exponentiation significantly cuts down run time to about O(k log d) for large numbers where k is the number of witnesses
        x = pow(witness, d, n)

        # x = witness**d % n ==> Runs in O(d) time which will slow things down drastically for large numbers

        if (x == 1) or (x == n - 1):
            continue

        # Squaring loop check
        for _ in range(1, s):
            x = (x**2) % n
            if x == 1:
                return False
            if x == (n - 1):
                return True

        return False

    return True


primes = [2, 3, 5, 7, 11, 13, 97, 104729]
composites = [1, 4, 9, 15, 100, 104730]

print("Primes:")
for p in primes:
    print(f"{p} - {miller_rabin(p)}")

print("Composites:")
for c in composites:
    print(f"{c} - {miller_rabin(c)}")
