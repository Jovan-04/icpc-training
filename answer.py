n = max(map(int, input().split()))
tasks = sorted(input().split())
inter = sorted(input().split())

count = 0
pt = 0
pi = 0

for _ in range(n+1):
    if pt == len(tasks) or pi == len(inter): break
    t = tasks[pt]
    i = inter[pi]
    if t <= i:
        count += 1
        pt += 1
    pi += 1

print(count)
