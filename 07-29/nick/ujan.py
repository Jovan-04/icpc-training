from collections import defaultdict
from itertools import combinations
from sys import stdin

n, q = map(int, stdin.readline().split())

trees = []
x_dict = defaultdict(list)
y_dict = defaultdict(list)
for _ in range(n):
    x, y, height = map(int, stdin.readline().split())
    tree_id = len(trees)
    trees.append(height)
    x_dict[x].append(tree_id)
    y_dict[y].append(tree_id)

x_trees = sorted(x_dict.items())
y_trees = sorted(y_dict.items())

def contains_triangle(x0, y0, x1, y1) -> bool:
    if (
        x0 > x_trees[-1][0] or x1 < x_trees[0][0]
        or y0 > y_trees[-1][0] or y1 < y_trees[0][0]
    ):
        return False

    l, h = 0, len(x_trees)
    while l < h:
        mid = (l + h) // 2
        x = x_trees[mid][0]
        if x < x0:
            l = mid + 1
        elif x > x0:
            h = mid
        else:
            l = mid
            break
    x_start = l
    
    l, h = l, len(x_trees)
    while l < h:
        mid = (l + h) // 2
        x = x_trees[mid][0]
        if x < x1:
            l = mid + 1
        elif x > x1:
            h = mid
        else:
            l = mid
            break
    x_stop = l + 1
    
    contained_trees = {
        t 
        for _, ids in x_trees[x_start:x_stop]
        for t in ids
    }

    l, h = 0, len(y_trees)
    while l < h:
        mid = (l + h) // 2
        y = y_trees[mid][0]
        if y < y0:
            l = mid + 1
        elif y > y0:
            h = mid
        else:
            l = mid
            break
    y_start = l
    
    l, h = l, len(y_trees)
    while l < h:
        mid = (l + h) // 2
        y = y_trees[mid][0]
        if y < y1:
            l = mid + 1
        elif y > y1:
            h = mid
        else:
            l = mid
            break
    y_stop = l + 1

    contained_trees &= {
        t 
        for _, ids in y_trees[y_start:y_stop]
        for t in ids
    }
    
    if len(contained_trees) < 3:
        return False
    
    heights = [trees[i] for i in contained_trees]
    for a, b, c in combinations(heights, 3):
        if abs(a - b) < c < a + b:
            return True
    return False

for _ in range(q):
    region = map(int, stdin.readline().split())
    print(int(contains_triangle(*region)))
