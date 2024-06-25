from sys import stdin


k, n = stdin.readline().split()
k = int(k)
n = int(n)

cards = stdin.readline().split()
cards = [int(card) for card in cards]
cards.sort()
print(cards)

def isSequential(seq):
    if len(seq) == 1:
        return True
    
    prev_n = seq[0]
    for n in seq[1:]:
        if prev_n + 1 != n:
            return False
        prev_n += 1
    return True



def isFair(k, n, cards):

    if n % k != 0:
        return False
    
    div = int(n / k)
    for i in range(div):
        if not isSequential(cards[(i)*k : (i+1)*k]):

            return False
    return True

if isFair(k, n, cards):
    print("fair")
else:
    print("unfair")