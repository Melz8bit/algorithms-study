import random


def solitaire_simulation(iterations: int):
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = [(rank, suit) for rank in ranks for suit in suits]

    half = len(deck) // 2

    winnable_count = 0
    for _ in range(iterations):
        random.shuffle(deck)
        half_deck_set = set(deck[:half])
        if (
            ("A", "hearts") in half_deck_set
            and ("A", "diamonds") in half_deck_set
            and ("A", "clubs") in half_deck_set
            and ("A", "spades") in half_deck_set
        ):
            winnable_count += 1

    print(winnable_count / iterations)


solitaire_simulation(100000)
