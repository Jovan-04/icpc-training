from sys import stdin

n, root = map(int, stdin.readline().split())
a, b = map(int, stdin.readline().split())

paths = {root: (None, None)}
for line in stdin:
    parent, left, right = map(int, line.split())
    if left:
        paths[left] = (parent, 'L')
    if right:
        paths[right] = (parent, 'R')

def find(value):
    path = []
    while value:
        value, direction = paths[value]
        path.append(direction)
    return path[::-1]

a_path = find(a)
b_path = find(b)

i = j = 0
while i < len(a_path) and j < len(b_path):
    if a_path[i] != b_path[j]:
        break
    i += 1
    j += 1

path = []
for _ in a_path[i:]:
    path.append('U')

for step in b_path[j:]:
    path.append(step)

print(''.join(path))
