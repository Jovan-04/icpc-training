from itertools import pairwise
from sys import stdin


def mountainous(nums: list[int]) -> bool:
    pairs = pairwise(nums)
    for a, b in pairs:
        if a == b:
            return False
        if a > b:
            break
    else:
        return False

    for a, b in pairs:
        if a <= b:
            return False

    return True


def palindromic(nums: list[int]) -> bool:
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] != nums[j]:
            return False
        i += 1
        j -= 1
    return True


def works(length: int, array: list[int]) -> bool:
    for i in range(len(array) - length + 1):
        subarray = array[i:i+length]
        if palindromic(subarray) and palindromic(subarray):
            return True
    return False


def min_length(array: list[int]) -> int:
    if not works(3, array):
        return -1

    def even(n):
        return n % 2 == 0

    n = len(array)
    low, high = 3, n - 1 if even(n) else n
    while low < high:
        mid = (low + high) // 2
        if even(mid):
            mid += 1

        if works(mid, array):
            low = mid
        else:
            high = mid - 2

    return high if works(high, array) else low


stdin.readline()
array = [int(line) for line in stdin]
print(min_length(array))
