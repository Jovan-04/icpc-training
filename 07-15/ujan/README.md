# Problem

The International Cherry Picking Contest (ICPC) is being held in your hometown
this year! The local team needs your help building a cherry-picking robot.

The robot, which will be placed somewhere in a binary cherry tree, can move
left, right, and up. For example, in the tree drawn below, if the robot is at
cherry 2, it can move up to cherry 1, left to cherry 3, or right to cherry 4.

```
    1
   / \
  2   5
 / \
3   4
```

Your task is to write a program that will find the shortest path the robot can
take between two cherries in a given tree.

## Input

The input consists of a single test case as described below.

The first line contains two integers `n` and `r`, as follows:

-   `n` (2 ≤ `n` ≤ 10^5), the number of cherries in the tree (cherries are
    numbered from 1 to `n`)
-   `r` (1 ≤ `r` ≤ `n`), the cherry at the root of the tree

The second line contains two integers `a` and `b` (1 ≤ `a`, `b` ≤ `n`, `a` ≠
`b`). The robot is initially placed at cherry `a` and must move to cherry `b`.

The next `n` lines describe the cherries. Each line contains three integers `x`,
`y`, and `z` (1 ≤ `x` ≤ `n`, 0 ≤ `y`, `z` ≤ `n`), indicating that cherry `x`'s
left child is cherry `y` and that its right child is cherry `z` (if `y` = 0,
cherry `x` does not have a left child; if `z` = 0, it does not have a right
child).

### Sample input

```
5 1
2 5
1 2 5
2 3 4
3 0 0
4 0 0
5 0 0
```

## Output

Output a single string describing the shortest path the robot can take from
cherry `a` to cherry `b`, with directions represented by the characters `L`
(left), `R` (right), and `U` (up).

### Sample output

```
UR
```

## Credits

This problem is based on [LeetCode #2096](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another).
