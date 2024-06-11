from sys import stdin

def generate_combinations(n):
    base_list = []
    for i in range(n - 1):
        base_list.append(-1)

    queue = [base_list]
    seen =  []
    while queue != []:
        curr_list = queue.pop()
        if curr_list not in seen:
            seen.append(curr_list)
            for i in range(n - 1):
                temp_list = curr_list.copy()
                temp_list[i] *= -1
                if temp_list not in seen:
                    queue.append(temp_list)
    return seen

def get_sums(integers, signs):
    sums = []
    for sign_list in signs:
        curr_sum = integers[0]
        for i in range(n - 1):
            curr_sum += integers[i + 1] * sign_list[i]
        sums.append(curr_sum)
    return sums


def is_divisible_by(sums, k):
    for sum in sums:
        if sum % k == 0:
            return True
    return False

case_count = int(stdin.readline().strip())

for i in range(case_count):

    n, k = stdin.readline().split()

    n = int(n.strip())
    k = int(k.strip())

    integers = stdin.readline().split()
    integers = [int(_.strip()) for _ in integers]

    signs = generate_combinations(n)
    sums = get_sums(integers, signs)

    if is_divisible_by(sums, k):
        print("Divisible")
    else:
        print("Not Divisible")