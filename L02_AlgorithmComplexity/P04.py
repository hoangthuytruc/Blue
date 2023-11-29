if __name__ == '__main__':
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = j = count = 0
    pairs = []

    while i < n and j < m:
        if a[i] - x <= b[j] <= a[i] + y:
            count += 1
            pairs.append((i + 1, j + 1))
            j += 1
            i += 1
        elif a[i] - x > b[j]:
            j += 1
        elif a[i] + y < b[j]:
            i += 1

    print(count)
    for element in pairs:
        print(element[0], element[1])