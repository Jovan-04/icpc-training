from math import ceil, log2
from sys import stdin

n = int(stdin.readline())
print(1 + ceil(log2(n)))
