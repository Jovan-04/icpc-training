def solve_ttt_case(line: str) -> str:
    r1 = tuple(*line[0:3].split())
    r2 = tuple(*line[3:6].split())
    r3 = tuple(*line[6:9].split())
    c1, c2, c3 = zip(r1, r2, r3)

    print(r1, r2, r3, sep='\n')
    print(c1, c2, c3)

    x_wins = False
    o_wins = False

    if ('X', 'X', 'X') in [r1, r2, r3, c1, c2, c3]: # check rows & cols
        x_wins = True
    if (r1[0] == r2[1] == r3[2] == 'X') or (r1[2] == r2[1] == r3[0] == 'X'): # check diags
        x_wins = True

    if ('O', 'O', 'O') in [r1, r2, r3, c1, c2, c3]:
        o_wins = True
    if (r1[0] == r2[1] == r3[2] == 'O') or (r1[2] == r2[1] == r3[0] == 'O'):
        o_wins = True


    if not is_possible(line, x_wins, o_wins):
        return '-1 -1'

    if x_wins:
        return '1 0'
    if o_wins:
        return '0 1'

    # and now for calculating the number of possible games...do we really have to generate the whole tree?

    return 'idk man'

def is_possible(line: str, x_wins: bool, o_wins: bool) -> bool:
    # taking turns means there can never be a diff of more than one
    xs = line.count('X')
    os = line.count('O')
    if abs(xs - os) > 1:
        return False

    if x_wins and o_wins:
        return False
    return True

def main():
    n = int(input())
    for _ in range(n):
        case = input()
        soln = solve_ttt_case(case)
        print(soln)

if __name__ == '__main__':
    main()