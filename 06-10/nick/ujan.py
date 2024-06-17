# This does not work!

from sys import stdin

def safe(W, S, C, K):
    if K == 0:
        return False
    
    return S <= K or W + C <= K

W, S, C, K = map(int, stdin.readline().split())
if safe(W, S, C, K):
    print('YES')
else:
    print('NO')
