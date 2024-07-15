# Problem

The International Collegiate Pattern Crackers (ICPC) have recently taken an
interest in strings, and they need your help to test their new pattern-matching
software.

The software uses two special characters in its patterns:

- `?` matches any character
- `*` matches any sequence of characters (even the empty sequence)

For example, the pattern `a?c` matches the string `abc` (but not `abbc`). The
pattern `a*c` matches the strings `ac`, `abc`, and `abbc` (but not `a` or `ab`).

Your task is to write a program that, given a string `s` and a pattern `p`,
determines whether ICPC's pattern-matching software should consider `p` to match
`s`.

## Input

The input consists of no more than 10 test cases. Each test case is a single
line containing two strings, `s` and `p`, separated by a single space. `s`
contains only lowercase letters. `p` contains only lowercase letters, `?`, and
`*`. Neither string's length exceeds 2000 characters.

### Sample input

```
abc a
abc a?c
abc *
```

## Output

For each test case, output a single line containing `true` if `p` matches `s`,
and `false` otherwise.

### Sample output

```
false
true
true
```

## Credits

This problem is based on [LeetCode #44](https://leetcode.com/problems/wildcard-matching/).
