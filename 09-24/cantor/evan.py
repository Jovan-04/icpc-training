def main():
    while True:
        line = input()
        if line == 'END':
            break

        if cantor(int(line)):
            print('MEMBER')
        else:
            print('NON-MEMBER')

def cantor(n: int) -> bool:
    print()
    return True

def int_to_base(n: int, b: int) -> list[int]:
    if n == 0:
        return [0]
    digits: list[int] = []
    while True:
        # digits.append()
        pass

if __name__ == '__main__':
    main()