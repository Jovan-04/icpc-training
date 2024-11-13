from sys import stdin

def fosh_week():
    input()
    students = [*map(int, stdin.read().splitlines())]
    # students = [9, 2, 3, 8, 5, 6, 1]
    n = 0

    for i in range(len(students)):
        for j in range(len(students) - 1):
            if students[j] > students[j+1]:
                n += 1
                tmp = students[j]
                students[j] = students[j+1]
                students[j+1] = tmp

    print(students)
    print(n)
                


fosh_week()