from sys import stdin
from re import fullmatch

def main():
  for line in stdin.read().splitlines():
    print('true' if cheat_matches(*line.split()) else 'false')

# waaaaaaay too slow.... what optimizations can we make in this solution that standard regex can't
def cheat_matches(string: str, pattern: str) -> bool:
  reg = pattern.replace('?', '.').replace('*', '.*')
  obj = fullmatch(reg, string)
  return bool(obj)
  

if __name__ == '__main__':
  main()