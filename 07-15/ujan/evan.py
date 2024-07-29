from sys import stdin

class BinaryTree:
    def __init__(self, val: int):
        self.value: int = val
        self.parent: BinaryTree | None
        self.left: BinaryTree | None
        self.right: BinaryTree | None

    def add(self, left: int, right: int):
        '''
        adds a left and right child to the tree. an input value of `0` means that there's no child.
        '''
        if left == 0:
            self.left = None
        else:
            l = BinaryTree(left)
            l.parent = self
            self.left = l

        if right == 0:
            self.right = None
        else:
            r = BinaryTree(right)
            r.parent = self
            self.right = r

    def __contains__(self, val: int) -> bool:
        if self.value == val:
            return True
        return ((val in self.left) if self.left else None) or ((val in self.right) if self.right else None)

    def sub_search(self, val: int) -> 'BinaryTree | None':
        '''
        searches for a value `val` in the tree and returns the subtree with `val` as the root. does not include nodes up the tree heirarchy
        '''
        if self.value == val:
            return self

        return (self.left.sub_search(val) if self.left else None) or (self.right.sub_search(val) if self.right else None)

    def path_to(self, to: int, path: list[str]) -> list[str]:
        if self.value == to:
            return path
        return ((self.left.path_to(to, [*path, 'L'])) if self.left else None) or ((self.right.path_to(to, [*path, 'R'])) if self.right else None)
    
    def path_from_to(self, from_: int, to: int) -> list[str]:
        root_to_a = self.path_to(from_, [''])
        root_to_b = self.path_to(to, [''])

        ind = next((i for i, (x, y) in enumerate(zip(root_to_a, root_to_b)) if x != y), min(len(root_to_a), len(root_to_b)))
        
        part_a = root_to_a[ind:] # needs to be reversed (converted to 'U's)
        part_b = root_to_b[ind:]

        rev_a = ['U' * len(part_a)]

        rev_a.extend(part_b)

        return rev_a

    def full_search(self, val: int) -> 'BinaryTree | None':
        '''
        searches for a value `val` in the tree and returns the subtree with `val` as the root
        '''
        pass

    def __str__(self) -> str:
        return str(self.value) + str(self.left) + str(self.right)

def main():
    n, r = map(int, input().split())
    a, b = map(int, input().split())
    tree_lines = stdin.read().splitlines()
    tree = BinaryTree(r)

    for line in map(str.split, tree_lines):
        (v, l, r) = map(int, line)
        tree.sub_search(v).add(l, r)

    path = tree.path_from_to(3, 4)
    print(''.join(path))

if __name__ == '__main__':
    main()
    # pass