from sys import stdin

MOD = 1_000_000_007

def cached(f):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = f(*args)
        cache[args] = result
        return result

    return wrapper

@cached
def rolls(dice: int, faces: int, target: int) -> int:
    if target < dice:
        return 0
    if target == dice:
        return 1
    if target == dice*faces:
        return 1
    if target > dice*faces:
        return 0

    return sum(rolls(dice-1, faces, target-roll) for roll in range(1, faces+1))

for line in stdin:
    dice, faces, target = map(int, line.split())
    print(rolls(dice, faces, target) % MOD)
