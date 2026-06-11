import math
import random


def pi_approximate(num_darts: int) -> float:
    circle_hits = 0
    for i in range(num_darts):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if ((x**2) + (y**2)) <= 1:
            circle_hits += 1

    return (circle_hits / num_darts) * 4


print(pi_approximate(100))  # rough — could be anywhere from 2.8 to 3.5
print(pi_approximate(1000))  # better — closer to 3.14
print(pi_approximate(10000))  # good — within ~0.05 of π
print(pi_approximate(1000000))  # very close — within ~0.001 of π
print(math.pi)
