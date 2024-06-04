from typing import Iterator
from sys import stdin


def paths(source: int, dest: int, map: list[list[int]], visited: list[int]) -> Iterator[list[int]]:
    streets = {street for street in map[dest] if street not in set(visited)}
    if source in streets:
        yield [source, *visited]

    for street in streets:
        yield from paths(source, street, map, [street, *visited])


streets = [[] for _ in range(21 + 1)]

head, *lines = stdin

fire = int(head)
for line in lines:
    a, b = map(int, line.split())
    streets[a].append(b)
    streets[b].append(a)

for path in paths(1, fire, streets, [fire]):
    print(' '.join(map(str, path)))
