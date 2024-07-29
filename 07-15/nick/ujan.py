from sys import stdin

rows, cols = map(int, stdin.readline().split())

def move(location, direction):
    r, c = location
    match direction:
        case '^':
            dr, dc = -1, 0
        case 'v':
            dr, dc = 1, 0
        case '>':
            dr, dc = 0, 1
        case '<':
            dr, dc = 0, -1
    r += dr
    c += dc

    return (r, c) if 0 <= r < rows and 0 <= c < cols else None

waters = []
lands = set()
sights = {(r, c): set() for r in range(rows) for c in range(cols)}
destinations = {(r, c): None for r in range(rows) for c in range(cols)}

for r, row in enumerate(stdin):
    for c, cell in enumerate(row.strip()):
        location = r, c
        match cell:
            case '#':
                for direction in '^v><':
                    if result := move(location, direction):
                        sights[result].add(location)

                lands.add(location)
            case '.':
                lands.add(location)
            case _:
                destinations[location] = move(location, cell)
                waters.append(location)

ever_visited = set()
best = 0
for location in waters:
    if location in ever_visited:
        continue

    visited = set()
    seen = set()
    while location and location not in visited and location not in lands:
        seen |= sights[location]
        visited.add(location)
        ever_visited.add(location)
        location = destinations[location]
    best = max(best, len(seen))

print(best)
