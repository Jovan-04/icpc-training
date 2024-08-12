from itertools import combinations

def main():
    n, q = map(int, input().split())
    forest = []
    for _ in range(n):
        tree = tuple(map(int, input().split()))
        forest.append(tree)
    print(forest)

    for _ in range(q):
        coords = map(int, input().split())
        print(1 if triangle_in_forest(forest, *coords) else 0)

def triangle_in_forest(forest: list, x1: int, y1: int, x2: int, y2: int) -> bool:
    valid_trees = filter(lambda tree: tree[0] >= x1 and tree[0] <= x2 and tree[1] >= y1 and tree[1] <= y2, forest)
    for c in combinations(valid_trees, 3):
        if valid_triangle(c):
            return True
    return False

def valid_triangle(c) -> bool:
    if any(t[2] == 0 for t in c): # triangles can't have a side length of zero
        return False
    t1, t2, t3 = sorted(c, key= lambda t: t[2])
    if t1[2] + t2[2] > t3[2]:
        return True
    return False

if __name__ == '__main__':
    main()