from sys import stdin

def main():
  n, k = map(int, stdin.readline().split())
  [num1, *nums] = [*map(int, stdin.readline().split())]

  num_possibilites = 2**(n-1)

  # initialize empty array to store all our totals
  totals = [num1] * num_possibilites
  for i, num in enumerate(nums):
    p = 0
    plus = True
    for _ in range(num_possibilites // (i+1)):
      for _ in range(2**i):
        totals[p] += (num if plus else -num)
        p += 1
      plus = not plus

  # totals is now a list containing all possible combinations of + and -, added up
  for t in totals:
    if t % k == 0:
      print("Divisible")
      return
  
  print("Not divisible")


if __name__ == '__main__':
  main()