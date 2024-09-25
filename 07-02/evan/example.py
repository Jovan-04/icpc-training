from copy import deepcopy

class Graph: 

    def __init__(self, vertices: int): 
        self.V = vertices 
        self.edges: list[list[float]] = [[None] * vertices for _ in range(vertices)]
    
    def get_edges(self):
        return self.edges
    
    def get_edge(self, fr: int, to: int) -> float:
        return self.edges[fr][to]
    
    def add_edge(self, fr: int, to: int, wt: float, undirected=True):
        self.edges[fr][to] = wt
        if undirected:
            self.edges[to][fr] = wt
    
    def remove_edge(self, fr: int, to: int, undirected=True):
        self.edges[fr][to] = None
        if undirected:
            self.edges[to][fr] = None
    
    def minimum_spanning_tree_length(self) -> float:
        temp = deepcopy(self.edges)
        total: float = 0
        while True:
            cur_min = 999999999
            i_min = 0
            j_min = 0
            for i, row in enumerate(temp):
                for j, col in enumerate(temp):
                    val = temp[i][j]
                    if val == None: continue
                    if cur_min > val:
                        cur_min = val
                        i_min = i
                        j_min = j
            if cur_min == 999999999: break
            total += cur_min
            temp[i_min][j_min] = None
            temp[j_min][i_min] = None
        return total



from sys import stdin

def main():
    num_cases = int(input())

    cases = stdin.read().split('\n\n')

    for case in cases:
        _, n, *points = case.splitlines()
        ans = solve_case(int(n), [*map(str.split, points)])
        print(ans)

def solve_case(n: int, points: list[list[str]]) -> float:
    g = Graph(n)
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i+1:], i+1):
            g.add_edge(i, j, dist_sqd(p1, p2))
    
    return g.minimum_spanning_tree_length()
    
def dist_sqd(p1: list[str], p2: list[str]) -> float:
    # order of subtraction doesn't matter b/c we're squaring the distances at the end
    dx = float(p1[0]) - float(p2[0])
    dy = float(p1[1]) - float(p2[1])
    return dx * dx + dy * dy
 
if __name__ == '__main__': 
    main()