from sys import stdin

def main():
    n = int(input())
    unique_times = set()
    total_starts = 0
    for line in stdin.read().splitlines():
        hours, minutes, seconds = line.split()
        hours = handle_thing(hours, 24)
        minutes = handle_thing(minutes, 60)
        seconds = handle_thing(seconds, 60)
        for h in hours:
            for m in minutes:
                for s in seconds:
                    unique_times.add((h, m, s))
                    total_starts += 1
    print(len(unique_times), total_starts)

        

def handle_thing(s: str, max: int):
    if s == '*':
        return range(max)
    else:
        nums = []
        for val in s.split(','):
            if '-' in val:
                x, y = map(int, val.split('-'))
                for n in range(x, y+1):
                    nums.append(n)
                continue
            nums.append(int(val))

        return nums
    
main()