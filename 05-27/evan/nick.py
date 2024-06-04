from sys import stdin

def bfs(edges):
    queue = [[1]]
    seen = []

    while queue != []:
        curr_path = queue.pop()
        if curr_path[-1] == target:
            seen.append(curr_path)
        else:
            for _ in edges[curr_path[-1]]:
                temp_list = curr_path.copy()
                temp_list.append(_)
                if _ not in curr_path:
                    queue.append(temp_list)
    return seen

lines = stdin.readlines()
while lines:
    edges = {}
    target = int(lines.pop(0).strip())
    currline = ""

    while currline.strip() != "0 0":
        currline = lines.pop(0)
        s, e = currline.split()
        s = int(s.strip())
        e = int(e.strip())

        if s in edges.keys():
            edges[s].append(e)
        else:
            edges[s] = [e]
        
        if e in edges.keys():
            edges[e].append(s)
        else:
            edges[e] = [s]
    
    for path in bfs(edges):
        temp_str = ""
        for corner in path:
            temp_str += str(corner) + " "
        print(temp_str)
    print("\n")