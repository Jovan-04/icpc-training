from dataclasses import dataclass


@dataclass
class Node:
    name: str
    parent: 'Node | None' = None
    count: int = 0
    left: 'Node | None' = None
    right: 'Node | None' = None

    def consume(self, ants: int | None = None):
        if self.count == 0:
            return

        ants = ants or self.count
        if self.left:
            self.left.consume(ants)
        if self.right:
            self.right.consume(ants)
        self.count -= ants


root = Node('a')
seen = {'a': root}
leaves = []

path_count, probe_count = map(int, input().split())
for _ in range(path_count):
    parent = root
    head, *rest = input().split()
    segment_count = int(head)
    for _ in range(segment_count):
        direction, _, path_count, name, *rest = rest
        count = int(path_count)
        if name in seen:
            parent = seen[name]
            continue
        node = Node(name, parent, count + parent.count)
        match direction:
            case 'L':
                parent.left = node
            case 'R':
                parent.right = node
        seen[name] = node
        parent = node
    leaves.append(name)

total = 0
for _ in range(probe_count):
    name = max(leaves, key=lambda x: seen[x].count)
    node = seen[name]
    total += node.count
    while node is not root:
        node.consume()
        node = node.parent
print(total)
