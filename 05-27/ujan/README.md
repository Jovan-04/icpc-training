# Problem

You have come to cheer on your friend at Icarus' Crazy Parachute Challenge
(ICPC)! However, the challenge is not what you expected.

At ICPC, players take turns jumping out of a plane. Each player is given dice
and a target number. After jumping out of the plane, the player rolls the dice.
If the sum of the dice is equal to the target number, the player wins the
challenge. Otherwise, the game continues with the next player.

Your task is to find the number of ways that a player can win the challenge.

## Input

The input consists of no more than 100 test cases. Each test case is described
by a single line containing three positive integers:

-   the number of dice (no more than `30`)
-   the number of faces on each die (no more than `30`)
-   the target number (no more than `1000`)

### Sample input

```
1 6 3
2 6 7
30 30 500
```

## Output

For each test case, output a single line containing the number of ways that a
player can win the challenge. Since this number may be very large, output it
modulo `10^9 + 7`.

### Sample output

```
1
6
222616187
```

## Credits

This problem is based on [LeetCode #1155](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/).
