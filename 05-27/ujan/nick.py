def numRollsToTarget(n: int, k: int, target: int) -> int:
    base_list = []
    for i in range(n):
        base_list.append(1)
    

        
    queue = [base_list]
    seen  = []
    count = 0
    while queue != []:
        curr_list = queue.pop()
        
        for i in range(n):
            temp_list = curr_list.copy()
            temp_list[i] += 1
            curr_sum = sum(temp_list)
            if curr_sum == target and temp_list not in seen:
                count += 1
                print(count)
                seen.append(temp_list)
            if temp_list[i] < k and curr_sum < target:
                queue.append(temp_list)
    return count & (10**9 + 7)


num = numRollsToTarget(n = 30, k = 30, target = 500)
print(num)