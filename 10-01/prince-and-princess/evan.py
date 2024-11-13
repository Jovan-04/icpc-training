def solve_case(i: int):
    n, p, q = map(int, input().split())
    prince = [*map(int, input().split())]
    princess = [*map(int, input().split())]

    prince_seen = set()
    princess_seen = set()

    prince_index = 0 # keeps track of where in each list we are
    princess_index = 0

    common_length = 0

    while True:
        prince_seen.add(prince[prince_index])
        princess_seen.add(princess[princess_index])

        if prince[prince_index] in princess_seen or princess[princess_index] in prince_seen:
            prince_seen.clear()
            princess_seen.clear()
            common_length += 1

        prince_index += 1
        princess_index += 1

        # end of both lists
        if prince_index >= len(prince) and princess_index >= len(princess):
            break

        if prince_index >= len(prince):
            prince_index -= 1
        
        if princess_index >= len(princess):
            princess_index -= 1

    print(f"Case {i}: {common_length}")


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        solve_case(i+1)