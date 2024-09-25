import sys
import math
from datetime import datetime

MAX = 1010

mas = [0] * MAX
x = [0.0] * MAX
y = [0.0] * MAX
MST = 0.0

e = []

def Repr(n):
    while n != mas[n]:
        n = mas[n]
    return n 

def Union(x, y):
    x1 = Repr(x)
    y1 = Repr(y)
    mas[x1] = y1
    return x1 != y1

def RunMST():
    res = 0.0
    for edge in e:
        if Union(int(edge[0]), int(edge[1])):
            res += math.sqrt(edge[2])
    return res

def main():
    num_cases = int(sys.stdin.readline())

    for _ in range(num_cases):
        dt = datetime.now()
        print(dt.minute, dt.second, dt.microsecond / 1000) # h/s/ms

        sys.stdin.readline()
        global MST
        n = int(sys.stdin.readline().strip())

        for i in range(1, n + 1):
            x[i], y[i] = map(float, sys.stdin.readline().strip().split())

        for i in range(1, n + 1):
            mas[i] = i

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                temp = [i, j, ((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2)]
                e.append(temp)

        e.sort(key=lambda a: a[2])
        MST = RunMST()

        print(f"{MST:.2f}")

if __name__ == "__main__":
    main()

