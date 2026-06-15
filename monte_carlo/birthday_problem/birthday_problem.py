import random


def birthday_problem(num_people: int, iterations: int):
    hits = 0
    for i in range(iterations):
        bdays = []
        for _ in range(num_people):
            bday = random.randint(1, 365)

            if bday in bdays:
                hits += 1
                break
            else:
                bdays.append(bday)

    return hits / iterations


print(birthday_problem(50, 100))
