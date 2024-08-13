from sys import stdin

def reachable(board):
    if board.count('X') - board.count('O') not in (0, 1):
        return False
    
    if won(board, 'X') and won(board, 'O'):
        return False
    
    return True

def cached(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

@cached
def won(board, player):
    return (
        player == board[0] == board[1] == board[2]
        or player == board[3] == board[4] == board[5]
        or player == board[6] == board[7] == board[8]
        or player == board[0] == board[3] == board[6]
        or player == board[1] == board[4] == board[7]
        or player == board[2] == board[5] == board[8]
        or player == board[0] == board[4] == board[8]
        or player == board[2] == board[4] == board[6]
    )

@cached
def winners(board, x_to_move):
    if won(board, 'X'):
        return 1, 0
    if won(board, 'O'):
        return 0, 1
    
    turn = 'X' if x_to_move else 'O'
    
    X, O = 0, 0
    for i, c in enumerate(board):
        if c == '.':
            x, o = winners(
                board[:i] + turn + board[i+1:],
                not x_to_move
            )
            X += x
            O += o
    
    return X, O

stdin.readline()
for line in stdin:
    board = line.strip()
    if not reachable(board):
        print('-1 -1')
        continue

    x_to_move = board.count('X') - board.count('O') == 0
    X, O = winners(board, x_to_move)
    print(X, O)
