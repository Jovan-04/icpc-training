# works, too slow :'c
from sys import stdin
from itertools import combinations

def main():
  n, k = map(int, stdin.readline().split())
  difficulties = sorted([*map(int, stdin.read().splitlines())])

  problem_sets = combinations(difficulties, k)
  
  count = 0
  for set_ in problem_sets:
    if is_nice(set_):
      count += 1
  print(count)

def is_nice(difficulties: list[int]) -> bool:
  if len(difficulties) < 3:
    return True
  a, b, n, *rest = difficulties
  if n <= a + b:
    return is_nice([b, n, *rest])
  else:
    return False

if __name__ == '__main__':
  main()