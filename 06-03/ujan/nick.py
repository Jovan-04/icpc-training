from sys import stdin



#Cycle through each edge and see if operation would increase or decrease the sum of those two nodes
#If it increased the sum, then make the change
def maximumValueSum(nums, k, edges):
        max_sum = sum(nums)
        prev_sum = -1

        count = 0
        change_made = True
        while change_made and max_sum >= prev_sum:
            change_made = False
            count += 1
            prev_sum = max_sum

            for edge in edges:
                u = nums[edge[0]]
                v = nums[edge[1]]

                bef_sum = u + v
                aft_sum = u ^ k + v ^ k

                if bef_sum < aft_sum:
                    #print(bef_sum, aft_sum)
                    nums[edge[0]] = u ^ k
                    nums[edge[1]] = v ^ k

                    max_sum = sum(nums)
                    print
                    change_made = True

        print(nums)
        return max_sum

nums = list(stdin.readline().split())
nums = [int(_) for _ in nums]

k = int(stdin.readline().strip())




#Read in from test file
edges = []
lines = stdin.readlines()
for line in lines:
    curr_line = line.split()
    temp_list = []
    for _ in curr_line:
        temp_list.append(int(_.strip()))
    edges.append(temp_list)
        

print(nums, k, edges)

print(maximumValueSum(nums, k, edges))