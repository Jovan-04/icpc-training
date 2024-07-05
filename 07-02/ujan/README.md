# Problem

The International Commission on Portable Containers (ICPC) is researching a new
device for collecting rainwater. The device sits on a platform and consists of
vertical bars between which water can be trapped. As the ICPC is considering
several competing designs, they have asked you to write a program that can
determine the area of water that can be trapped by a given design.

## Input

A device of width `w` can be represented by an elevation map, a list of `w`
integers representing the height of the device at each position. For example,
the elevation map `0,0,6,0,0` represents a device (`w` = 5) with a single bar of
height 6 in the middle.

The input consists of a single design. The first line contains an integer `w`
(1 ≤ `w` ≤ 10^5), the width of the device. The second line contains `w` integers
(0 ≤ `n` ≤ 10^4) separated by spaces, representing the elevation map.

### Sample input

```
12
0 1 0 2 1 0 1 3 2 1 2 1
```

## Output

Output the area of water that can be trapped by the design.

### Sample output

```
6
```

## Credits

This problem is based on [LeetCode #42](https://leetcode.com/problems/trapping-rain-water/).
