if __name__ == '__main__':
    n, w = map(int, input().split())
    cups = list(map(int, input().split()))
    cups.sort()

    m = min(cups[0], cups[n] / 2)
    total = 3 * m * n
    print(min(total, w))