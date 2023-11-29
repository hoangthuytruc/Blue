if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sum_energy = sum(a)
    left = 0
    right = 1000
    while right - left > 1e-7:
        mid = (left + right) / 2
        sum_transfer = 0
        for x in a:
            if x > mid:
                sum_transfer += x - mid
        if mid * n < sum_energy - sum_transfer * k / 100:
            left = mid
        else:
            right = mid
    print('%.9f' % left)