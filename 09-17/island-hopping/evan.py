import heapq

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def dist_sqd(self, other) -> float:
        return (self.y - other.y) ** 2 + (self.x - other.x) ** 2
    
    def __repr__(self) -> str:
        return f"Point(x: {self.x}, y: {self.y})"


def solve_case():
    points: list[Point] = []

    n = int(input())

    def read_points():
        for _ in range(n): # read in points
            points.append(Point(*map(float, input().split())))
    read_points()

    # initialize point dict
    dists: dict[Point, dict[Point, float]] = {}

    # calculate all distances
    def calc_dists():
        for p1 in points:
            dists[p1] = {}
            for p2 in points:
                if dists.get(p2, dict()).get(p1):
                    dists[p1][p2] = dists[p2][p1]
                d = p1.dist_sqd(p2)
                dists[p1][p2] = d
    calc_dists()

    # calculate MST
    MST_vertices: set[Point] = set()
    vertices_to_add: set[Point] = set(points)
    MST_length = 0.0

    # pick initial point
    ip = points[0]
    MST_vertices.add(ip)
    vertices_to_add.remove(ip)

    def minspt():
        nonlocal MST_length
        while True:
            min_dist = 999999999999999
            min_point = None

            # find closest point
            for origin in MST_vertices:
                for target in vertices_to_add:
                    
                    if dists[origin][target] < min_dist:
                        min_dist = dists[origin][target]
                        min_point = target

            # update the MST
            vertices_to_add.remove(min_point)
            MST_vertices.add(min_point)
            MST_length += min_dist ** 0.5

            if len(vertices_to_add) == 0:
                break
    minspt()

    print(MST_length)

def main():
    n = int(input())
    for _ in range(n):
        solve_case()

if __name__ == '__main__':
    main()