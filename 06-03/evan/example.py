from sys import setrecursionlimit

def moduloneg(a: int, b: int) -> int:
    # why not just check if the mod is negative and if so, add b?
    c = 0
    if a < b:
        a = -a
        c = a % b
        c = b - c
    else:
        c = a
    return c % b

DP = [[-1] * 10 for _ in range(10)]
n, k = map(int, input().split())
Tab = [*map(int, input().split())]

def Divis(modulo: int, pos: int) -> bool:
    if pos == n - 1:
        if (moduloneg(((-1) * Tab[pos] + modulo), k) == 0):
            DP[modulo][pos] = True
            return True

        if (moduloneg((Tab[pos] + modulo), k) == 0):
            DP[modulo][pos] = True
            return True

        DP[modulo][pos] = False
        return False
    
    elif (DP[modulo][pos] != -1):
        return DP[modulo][pos]
    else:
        if (Divis(moduloneg(Tab[pos] * (-1) + modulo, k), pos + 1) == True):
            DP[modulo][pos] = True
            return True

        if (Divis(moduloneg(Tab[pos] + modulo, k), pos + 1) == True):
            DP[modulo][pos] = True
            return True

        DP[modulo][pos] = False
        return False

def solve_case():
    if n == 1:
        if moduloneg(Tab[0], k) == 0:
            print("Divisible")
        else:
            print("Not divisible")
    else:
        if Divis(moduloneg(Tab[0], k), 1):
            print("Divisible")
        else:
            print("Not divisible")

# setrecursionlimit(10_010)
solve_case()