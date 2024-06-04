from sys import stdin

lines = stdin.readlines()

lines = [_.strip() for _ in lines]

def get_unique_chars(line):
    seen = []
    for char in line:
        if char not in seen:
            seen.append(char)

    return seen


def puq_substring_count(line, unique_chars):
    seen = []

    
    for i in range(len(line)):
        temp_unq = unique_chars.copy()
        for j in range(len(line)):
            if i < j:
                cur_sub = line[i:j]
                print(i,j)
                print(cur_sub)
                if line[j-1] in unique_chars and line[j-1] not in temp_unq:
                    break
                if line[j-1] in temp_unq:
                    print("Removing", line[j])
                    temp_unq.remove(line[j-1])
                
                print(temp_unq)
                if temp_unq == []:
                    if cur_sub not in seen:
                        seen.append(cur_sub)
                    break


    print(seen)

    return len(seen)

for line in lines:
    break
    print(puq_substring_count(line, get_unique_chars(line)))
print(puq_substring_count(lines[1], get_unique_chars(lines[1])))
    