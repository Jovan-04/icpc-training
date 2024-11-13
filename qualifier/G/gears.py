from math import log

def speedup(fm: int, to: int) -> float:
    return fm / to

def maximum_speedup(ratios: list[int]) -> float:
    ratios = sorted(ratios)
    max_spdup = 0.0
    L = len(ratios) // 2
    
    for i in range(L):
        max_spdup += log(speedup(ratios[-(i+1)], ratios[i]))

    return max_spdup

def main():
    gears: dict[int, list[int]] = {}

    for _ in range(int(input())):
        s, t = map(int, input().split())
        if not gears.get(s, False):
            gears[s] = []
        gears[s].append(t)

    max_spdup = 0.0
    for tooth_size in gears.values():
        max_spdup += maximum_speedup(tooth_size)

    print(max_spdup)

if __name__ == '__main__':
    main()