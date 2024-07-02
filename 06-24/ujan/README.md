# Problem

The International Construction Planning Committee (ICPC) has asked you to help
them select a country for their upcoming convention.

For each country, you are given a list of roads connecting cities. You must
assign each city a unique integer value from 1 to n in a way that maximizes the
country's importance.

A country's importance is defined as the sum of the importance of its roads. The
importance of a road connecting cities A and B is the sum of the values you've
assigned to A and B.

## Input

The first line of input contains two integers, `n`, the number of cities
(2 ≤ `n` ≤ 50000), and `m`, the number of roads (1 ≤ `m` ≤ 50000). The next `m`
lines each contain two integers `a` and `b` (1 ≤ `a`, `b` ≤ `n`, `a` ≠ `b`),
indicating that there is a road connecting cities `a` and `b`.

### Sample input

```
5 6
0 1
1 2
2 3
0 2
1 3
2 4
```

```
5 3
0 3
2 4
1 3
```

## Output

Output a single integer representing the maximum possible importance of the
country.

### Sample output

```
43
```

```
20
```

## Credits

This problem is based on [LeetCode #2285](https://leetcode.com/problems/maximum-total-importance-of-roads/).
