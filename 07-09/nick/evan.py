from math import gcd
from sys import stdin

class Tree:
  def __init__(self):
    self.children: list[Tree] = []

  def get_children(self):
    return self.children
  
  # how tf pls help
  def create_tree(nodes: list[int], edges: list[tuple[int]]):
    for edge in edges:
      pass

def main():
  n = int(input())
  inp = stdin.read().splitlines()
  nodes = [*map(int, inp[:n])]
  edges = [*map(lambda s: tuple(map(int, s.split())), inp[n:])]
  
  


if __name__ == '__main__':
  main()