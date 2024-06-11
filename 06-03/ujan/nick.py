from sys import stdin


lines = stdin.readlines()


lines = [line.split() for line in lines]

switch = False
group1 = []
group2 = []

for line in lines:
    if line == []:
        switch = True

    if not switch and line != []:
        group1.append(line)
    elif line != []:
        group2.append(line)


no_mismatches = True
for i in range(len(group1)):
    curgroup1firstname = group1[i][0].lower()
    curgroup1lastname = group1[i][1].lower()
    curgroup1address = group1[i][2].lower()

    no_match = True
    for j in range(len(group2)):
        curgroup2firstname = group2[j][0].lower()
        curgroup2lastname = group2[j][1].lower()
        curgroup2address = group2[j][2].lower()
        if (curgroup1firstname == curgroup2firstname and curgroup1lastname == curgroup2lastname) or curgroup1address == curgroup2address:
            no_match = False
    
    if no_match:
        print("I", curgroup1address, curgroup1lastname, curgroup1firstname)
        no_mismatches = False

for i in range(len(group2)):
    curgroup2firstname = group2[i][0].lower()
    curgroup2lastname = group2[i][1].lower()
    curgroup2address = group2[i][2].lower()
    no_match = True
    for j in range(len(group1)):
        curgroup1firstname = group1[j][0].lower()
        curgroup1lastname = group1[j][1].lower()
        curgroup1address = group1[j][2].lower()
        if (curgroup1firstname == curgroup2firstname and curgroup1lastname == curgroup2lastname) or curgroup1address == curgroup2address:
            no_match = False
    
    if no_match:
        print("O", curgroup2address, curgroup2lastname, curgroup2firstname)
        no_mismatches = False

if no_mismatches:
    print("No mismatches.")