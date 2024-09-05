def max_sum(nums: list[int], k: int, edges: list[list[int]]) -> int:
    current = sum(nums)
    updates = [(n ^ k) - n for n in nums]
    updates.sort(reverse=True)

    maximum = current
    i = 0
    while i + 1 < len(updates):
        update = updates[i] + updates[i + 1]
        if update <= 0:
            break

        maximum += update
        i += 2

    return maximum
