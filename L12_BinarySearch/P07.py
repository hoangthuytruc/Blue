def bs(a, x, left, right):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            return bs(a, x, mid + 1, right)
        else:
            return bs(a, x, left, mid - 1)
    return -1


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for e in a:
        pos = bs(a, e + k, 0, n - 1)
        if pos != -1:
            count += 1
    print(count)
