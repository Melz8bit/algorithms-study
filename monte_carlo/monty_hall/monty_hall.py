import random


def monty_hall(iterations: int):
    stay, swap = 0, 0
    for i in range(iterations):
        doors = [None] * 3
        doors[random.randint(0, 2)] = "x"

        # Player selects door
        user_door = random.randint(0, 2)

        is_winning = False
        if doors[user_door] == "x":
            is_winning = True

        # Remove losing door
        doors.remove(None)

        # Reassign user's door index
        user_door = doors.index("x") if is_winning else doors.index(None)

        # Player stays on their door
        if doors[user_door] == "x":
            stay += 1

        # Player swaps door
        user_door = 1 - user_door
        if doors[user_door] == "x":
            swap += 1

    results = {
        "stayed": (stay / iterations),
        "swapped": (swap / iterations),
    }

    return results


print(monty_hall(500000))
