from Movements import make_movement
import random

def make_shuffle(actual, n):
    for _ in range (n):
        m = random.randint(0, 12)
        i = random.randint(0, 1)
        make_movement(actual.cubo, m, i)
    return actual