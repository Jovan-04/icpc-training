import math
from datetime import datetime
# ~1ms to init and read input
# 200ms to calculate all distances
# 100ms to sort
# 700ms to build MST
# keeping track of vertices added brings MST down to 400ms...but it also gives me a different answer. and still not fast enough
# they gotta get better computers man

def solve_case():
    dt = datetime.now()
    # print(f"Starting at {dt.second}s {dt.microsecond / 1_000}ms")

    input() # consume blank line
    num = int(input()) # number of freckles

    MAX = num + 1 # max test case size
    mas = [*range(num + 1)]
    x = [0.0] * MAX
    y = [0.0] * MAX
    MST = 0.0
    e = []

    # VERTICES_INCLUDED = set()

    def Repr(n: int) -> int:
        while n != mas[n]:
            n = mas[n]
        return n
    
    def Union(x: int, y: int) -> bool:
        x1 = Repr(x)
        y1 = Repr(y)
        mas[x1] = y1
        return x1 != y1
    
    def RunMST() -> float:
        res = 0.0
        for edge in e:
            # cool optimization, but it doesn't give you the right answer as you can end up with stranded "pods" of vertices
            # if (edge[0] in VERTICES_INCLUDED) and (edge[1] in VERTICES_INCLUDED): continue
            if Union(int(edge[0]), int(edge[1])):
                # VERTICES_INCLUDED.add(edge[0])
                # VERTICES_INCLUDED.add(edge[1])
                res += math.sqrt(edge[2])
        return res

    for i in range(1, num + 1): # read all the freckles
        x[i], y[i] = map(float, input().split())

    dt = datetime.now()
    # print(f"input done at {dt.second}s {dt.microsecond / 1_000}ms")
    
    for i in range(1, num + 1):
        for j in range(i + 1, num + 1):
            temp = [i, j, ((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2)]
            e.append(temp)

    dt = datetime.now()
    # print(f"dists done at {dt.second}s {dt.microsecond / 1_000}ms")

    e.sort(key=lambda a: a[2])
    dt = datetime.now()
    # print(f"sorting done at {dt.second}s {dt.microsecond / 1_000}ms")

    MST = RunMST()
    dt = datetime.now()
    # print(f"MST done at {dt.second}s {dt.microsecond / 1_000}ms")

    print(f"{MST:.2f}")

def main():
    num_cases = int(input())

    for _ in range(num_cases):
        solve_case()

if __name__ == '__main__':
    main()