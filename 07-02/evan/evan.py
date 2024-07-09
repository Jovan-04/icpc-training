from sys import stdin

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  # no need for actual distance, and sqrt is slow
  def distance_sqd(self, other):
    dx = other.x - self.x
    dy = other.y - self.y
    return dx * dx + dy * dy

def main():
  num_cases = int(input())

  cases = stdin.read().split('\n\n')

  for case in cases:
    _, n, *points = case.splitlines()
    solution = solve_case(n, map(Point, points))
    print(solution, '\n')

# djikstra's algo + caching distances btwn points
def solve_case(n: int, points: list[Point]) -> float: 
  pass

if __name__ == '__main__':
  main()
