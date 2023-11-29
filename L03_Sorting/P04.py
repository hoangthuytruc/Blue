def printResult(a):
    if a - int(a) == 0:
        print(int(a))
    else:
        print(a)


if __name__ == '__main__':
    n, w = map(int, input().split())
    capacities = input()

    max = w / (3 * n)
    if max - int(max) < 0.5:
        print(int(max) * 3 * n)
    else:
        printResult((int(max) + 0.5) * 3 * n)