def main():
    c, t = map(int, input().split())
    cards = [*map(int, input().split())]

    for card in cards:
        rem_cs = cards[:]
        rem_cs.remove(card)
        search_ops(card, t , rem_cs)


def search_ops(curr_num: int, target_num: int, remaining_nums: list[int]):
    possible_ops = ['+', '-', '*', '/']
    print(remaining_nums)

def search_nums(curr_op: str, target_num: int, remaining_nums: list[int]):
    pass

main()