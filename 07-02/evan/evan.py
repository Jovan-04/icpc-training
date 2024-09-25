from sys import stdin

class Point:
  def __init__(self, line: str):
    x, y = map(float, line.split())
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
    print(points)
    solution = solve_case(n, [*map(Point, points)])
    print(solution, '\n')

# minimum spanning tree + caching distances btwn points
def solve_case(n: int, points: list[Point]) -> float:
  print(points)
  connections: dict[dict[float]] = {}
  for p1 in points:
    connections[p1] = dict()
    for p2 in points:
      if p1 ==  p2: continue
      connections[p1][p2] = p1.distance_sqd(p2)

  print(connections)


if __name__ == '__main__':
  main()
