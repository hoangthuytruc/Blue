def sumTrees(a, x):
    sum = 0
    for e in a:
        if e > x:
            sum += e - x
    return sum


def bsLast(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        sumMid = sumTrees(a, mid)
        if (mid == right or x > sumTrees(a, mid + 1)) and sumMid >= x:
            return mid
        elif x < sumMid:
            return bsLast(a, mid + 1, right, x)
        else:
            return bsLast(a, left, mid - 1, x)
    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    pos = bsLast(trees, 0, max(trees) + 1, m)
    print(pos)