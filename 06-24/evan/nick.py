from sys import stdin

line = stdin.readline().strip()
dictionary = []
while line != "":
    dictionary.append(line)
    line = stdin.readline().strip()

pairs = stdin.readlines()
pairs = [pair.split() for pair in pairs]

def isDoublet(word1, word2):
    foundOneDifference = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if not foundOneDifference:
                foundOneDifference = True
            else:
                return False
    if foundOneDifference:
        return True
    else:
        return False


def checkPair(start,end,dictionary):
    queue = [[start]]

    while queue:
        currentList = queue.pop()
        if currentList[-1] == end:
            yield currentList
        else:
            for word in dictionary:
                if word not in currentList:
                    if isDoublet(currentList[-1],word):
                        currentList.append(word)
                        queue.append(currentList)
    return

count = 0
for i in range(len(pairs)):
    pair = pairs[i]
    count += 1
    minLength = float("inf")
    ans = []
    for sol in checkPair(pair[0],pair[1], dictionary):
        if len(sol) < minLength:
            ans = sol
            minLength = len(sol)
    if minLength == float("inf"):
        print("No solution.")
        
    else:
        for word in ans:
            print(word)

    if i + 1 < len(pairs):
        print()