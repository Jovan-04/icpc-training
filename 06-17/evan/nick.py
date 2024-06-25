from sys import stdin

#Input
lines = stdin.readlines()
sequences = []
for line in lines:
    temp = []
    for num in line.split():
        temp.append(int(num))
    sequences.append(temp)



#Solution
for seq in sequences:
    
    
    nums = []
    for n in range(len(seq) - 2):
        nums.append(n + 1)
    for i in range(len(seq) - 1):
        #Length of 1 sequence
        if len(seq) == 1:
            break

        #
        if abs(seq[i] - seq[i + 1]) in nums:
            nums.remove(abs(seq[i] - seq[i + 1]))
    
    if nums == []:
        print("Jolly")
    else:
        print("Not jolly")
    