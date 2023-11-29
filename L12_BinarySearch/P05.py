import bisect


def canReachTop(a, k):
    count = k
    for i in range(0, len(a) - 1):
        d = a[i+1] - a[i]
        if d > k:
            return False
        elif d == k:
            count -= 1
    return count > 0


def bsFirst(a, left, right):
    if len(a) == 2:
        return a[1]

    if left <= right:
        mid = (left + right) // 2
        canReach = canReachTop(a, mid)
        if (mid == left or not canReachTop(a, mid - 1)) and canReach:
            return mid
        elif canReach:
            return bsFirst(a, left, mid - 1)
        else:
            return bsFirst(a, mid + 1, right)
    return -1


if __name__ == '__main__':
    Q = int(input())
    for i in range(Q):
        n = int(input())
        heights = list(map(int, input().split()))
        heights.insert(0, 0)
        pos = bsFirst(heights, 0, max(heights))
        print("Case {0}: {1}".format(i + 1, pos))