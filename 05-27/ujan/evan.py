def main():
  n = 1
  k = 6
  target = 3
  n = num_rolls_to_target(n, k, target)
  print(n)

def num_rolls_to_target(n: int, k: int, target: int) -> int:
  num = roll(n, k, target, 0, 0)

  return num % (10**9 + 7)

def roll(n: int, k: int, target: int, total: int):
  if n == 0:
    if total == target:
      return 1
    else:
      return 0

  for i in range(1, k+1):
    roll(n - 1, k, target, total + i)



if __name__ == '__main__':
  main()