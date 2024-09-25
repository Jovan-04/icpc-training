# problem: https://open.kattis.com/problems/leidangur - too slow :(

backpack: list[str] = []
journey = input()

for space in journey:
    if space == '.': continue

    if space in 'pgo':
        backpack.append(space)
        continue
    
    if space in 'PGO':
        if space.lower() in backpack:
            ri = [*reversed(backpack)].index(space.lower()) + 1
            backpack = backpack[:-ri]
        else:
            print("Neibb")
            exit()

print(backpack.count('p'))
print(backpack.count('g'))
print(backpack.count('o'))