from sys import stdin

def partitionable(hand, group_size):
    if len(hand) % group_size != 0:
        return False

    hand.sort()
    while hand:
        n = hand[0]
        try:
            for i in range(group_size):
                hand.remove(n+i)
        except ValueError:
            return False

    return True

k, n = map(int, stdin.readline().split())
hand = [int(card) for card in stdin.readline().split()]

if partitionable(hand, k):
    print('fair')
else:
    print('unfair')
