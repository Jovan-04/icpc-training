from sys import stdin

def main():
  input() # trash the first line
  total_importance = 0
  for a, b in map(lambda l: map(int, l.split()), stdin.read().splitlines()):
    total_importance += a + b
  print(total_importance)

if __name__ == '__main__':
  main()