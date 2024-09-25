# https://open.kattis.com/problems/taktsvedjur wrong answer, maybe I don't understand the problem?

from sys import stdin
from math import log2

def main():
    n = int(input())
    score = 0
    streak = 0
    multiplier = 1

    for line in map(int, stdin.read().splitlines()):
        print("executing line", line)
        print("mult", multiplier)
        print("score", score)
        # miss
        if line == 0:
            print("streak", streak, "lost")
            multiplier = round(multiplier / 2) # round so that a multiplier of 1 gets rounded back up to 1
            print("new multiplier of", multiplier)
            streak = 0
            continue
        # hit
        streak += 1
        print("streak now", streak)
        if log2(streak) % 1 == 0 and streak != 1:
            multiplier = min(streak, 800)
            print("new multiplier", multiplier)
        print("adding", line * multiplier, "score")
        score += line * multiplier

    print(score)


if __name__ == '__main__':
    main()