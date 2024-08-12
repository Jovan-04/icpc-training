from sys import stdin

def main():
    _, d = map(int, input().split())
    notes = map(int, stdin.read().splitlines())
    s_notes = sorted(set(notes))
    
    takes = 0
    while len(s_notes) != 0: # each recording take
        takes += 1

        original = s_notes.pop(0)
        for _ in range(d):
            if len(s_notes) == 0:
                return takes
            new = s_notes[0]
            if new - original <= d:
                s_notes.pop(0)
            else:
                break
    return takes
    

if __name__ == '__main__':
    print(main())