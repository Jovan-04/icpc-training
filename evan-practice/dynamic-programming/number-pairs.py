def find_pairs(S: list[int], target: int) -> tuple[int, int]:
    seen_numbers = set()

    for num in S:
        # calculate the number we need to make a pair
        diff = target - num

        # if we've already seen it, we have a solution
        if diff in seen_numbers:
            return (num, diff)
        # otherwise, mark it as seen
        else:
            seen_numbers.add(num)
    
    # no pairs in the list
    return None

if __name__ == '__main__':
    p = find_pairs([8, 10, 2, 9, 7, 5], 11)
    print(p)