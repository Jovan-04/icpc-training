from sys import stdin

def main():
    n = int(input())
    nums = {}
    for i in range(51):
        nums[i] = 0

    for num in map(int, stdin.read().split()):
        nums[num] += 1
    
    found = False
    for (k, v) in nums.items():
        if v > (2 * n):
            found = True
            print(k, end=' ')
    
    if not found:
        print("-1")

if __name__ == '__main__':
    main()