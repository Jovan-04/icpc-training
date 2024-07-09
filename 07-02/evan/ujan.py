from math import hypot
from sys import stdin

def read_case() -> list[tuple[float, float]]:
    def read_coordinate() -> tuple[float, float]:
        x, y = map(float, stdin.readline().split())
        return x, y

    stdin.readline()
    n = int(stdin.readline())
    return [read_coordinate() for _ in range(n)]

cases = int(stdin.readline())
for _ in range(cases):
    ink = 0

    freckles = read_case()
    connected = set()
    for i, (x, y) in enumerate(freckles):
        if (x, y) in connected:
            continue
        
        x2, y2 = min(
            freckles[:i] + freckles[i+1:],
            key=lambda f: hypot(x - f[0], y - f[1])
        )
        
        ink += hypot(x2 - x, y2 - y)
        
        connected.add((x, y))
        connected.add((x2, y2))
        
    print('%.2f' % ink)
    print()
