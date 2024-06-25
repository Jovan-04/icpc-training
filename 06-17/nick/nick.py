from sys import stdin

n = stdin.readline()
n = int(n)

alphabet = ['a','b']

base_str = ''
for i in range(n):
    base_str += 'a'
    
prev_str = base_str


for i in range(n):
    print(prev_str)
    temp_str = prev_str[:i] + 'b' + prev_str[i + 1:]
    prev_str = temp_str