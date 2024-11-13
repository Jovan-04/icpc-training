l, h = 0, 1001

while True:
    mid = (l + h) // 2
    print(mid)

    response = input()

    if response == "correct":
        break
    elif response == "lower":
        h = mid
    else:
        l = mid