def upper_part(num):
    for i in range(1, num + 1):
        print(f'{" " * (num - i)}{i * "* "}')


def bottom_part(num):
    for i in range(num - 1, 0, -1):
        print(f'{" " * (num - i)}{i * "* "}')


n = int(input())

upper_part(n)
bottom_part(n)