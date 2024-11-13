def divide_groceries(groceries: list[int], n: int, d: int) -> int:
    # DP[x1][x2] stores the price from x1 x2
    DP = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                DP[i][j] = 0

if __name__ == '__main__':
    n, d = map(int, input().split())
    groceries = map(int, input().split())
    price = divide_groceries(groceries, n, d)
    print(price)