from sys import stdin

_, limit = map(int, stdin.readline().split())
pitches = sorted({int(line) for line in stdin})

recordings = 0
while pitches:
    recordings += 1
    start = pitches.pop()
    try:
        while start - pitches[-1] <= limit:
            pitches.pop()
            continue
    except IndexError:
        break

print(recordings)
