import random


def dice_probability(num_dice: int, sides: int, target: int, iterations: int) -> float:
    hit = 0
    for x in range(iterations):
        roll = [random.randint(1, sides) for _ in range(num_dice)]
        if sum(roll) == target:
            hit += 1

    return hit / iterations


print(dice_probability(2, 6, 7, 100000))
