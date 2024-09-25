from random import randint

with open('bigcase.txt', 'a') as file:
    for _ in range(10_000):
        n = randint(-9_999, 9_999)
        file.write(str(n) + ' ')
