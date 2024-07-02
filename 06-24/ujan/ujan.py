from sys import stdin

n, m = map(int, stdin.readline().split())
roads = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

cities = {city: 0 for city in range(n)}
for a, b in roads:
    cities[a] += 1
    cities[b] += 1

importances = {
    city: i
    for i, city in enumerate(sorted(cities, key=lambda c: cities[c]), start=1)
}

print(sum(importances[a] + importances[b] for a, b in roads))
