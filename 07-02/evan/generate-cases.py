from random import random

def rf():
    return round(random() * 2_000 - 1_000, 3)

def main():
    output = ""

    output += "10\n"

    for _ in range(10):
        # output += "\n"
        output += "750\n"
        for _ in range(750):
            output += f"{rf()} {rf()}\n"


    with open("abigtestcase.txt", 'w') as file:
        file.write(output)

main()