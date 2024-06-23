from itertools import pairwise
from sys import stdin

def is_jolly(sequence: list[int]) -> bool:
    n = len(sequence)
    differences = set()

    for a, b in pairwise(sequence):
        diff = abs(a - b)
        if (diff > n - 1 or diff == 0 or diff in differences):
            return False

        differences.add(diff)

    return True

for line in stdin:
    _, *sequence = map(int, line.split())
    if is_jolly(sequence):
        print('Jolly')
    else:
        print('Not jolly')
