import random

tasks = []
inter = []
for i in range(200_000):
    tasks.append(random.choice(range(100_000, 199_999)))
    inter.append(random.choice(range(100_000, 199_999)))
    
with open('bigin.txt', 'w') as output:
    s = '200000 200000\n'
    s += ' '.join(map(str, tasks)) + '\n'
    s += ' '.join(map(str, inter))
    output.write(s)