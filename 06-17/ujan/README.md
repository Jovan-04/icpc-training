# Problem

You are participating in the Incredible Card Partition Challenge (ICPC). In the
first round, each player is given a hand of cards and a number `k`. The
objective is to split the hand into groups such that each group consists of `k`
consecutive cards. The first player to complete this task wins the round.

The ICPC organizers want to ensure that the game is fair. Your task is to
determine whether a player can win the challenge given a hand of cards and the
number `k`.

## Input

The input consists of two lines. The first line contains two integers: `k` and
the number of cards in the hand, `n`, where `1` ≤ `k` ≤ `n` ≤ `10^4`. The second
line consists of `n` integers, each representing the value of a card in the hand
(`1` ≤ `card` ≤ `10^9`).

### Sample input

```
3 9
1 2 3 4 5 6 7 8 9
```

```
4 5
1 2 3 4 5
```

## Output

If it's possible for a player to win the challenge, output `fair`. Otherwise,
output `unfair`.

### Sample output

```
fair
```

```
unfair
```

## Credits

This problem is based on [LeetCode #846](https://leetcode.com/problems/hand-of-straights/).
