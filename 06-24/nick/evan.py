from sys import stdin
from itertools import pairwise

def main():
  input()
  input_ = map(int, stdin.read().splitlines())
  result = mountainous_subarray([*input_])
  print(len(result))

def mountainous_subarray(array: list[int]) -> int:
  slope: list[int] = []
  heads = []
  tails = []

  for i, j in pairwise(array):
    if i < j: # we are going up the mountain
      slope.append(1)
    if i > j: # we are going down the mountain
      slope.append(-1)
    if i == j: # flat
      slope.append(0)

  print(slope)
  

  for (i, (a, b)) in enumerate(pairwise(slope), 1):
    if [a, b] == [-1, 1]: # start/end of the mountain
      pass
    if [a, b] == [1, -1]: # peak of the mountain
      pass

  return array

if __name__ == '__main__':
  main()