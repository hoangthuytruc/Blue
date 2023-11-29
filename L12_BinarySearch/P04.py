import bisect

if __name__ == '__main__':
    n = int(input())
    ladies = list(map(int, input().split()))
    m = int(input())
    queries = list(map(int, input().split()))
    for q in queries:
        posL = bisect.bisect_left(ladies, q)
        posR = bisect.bisect_right(ladies, q)
        a = ladies[posL - 1] if posL - 1 in range(n) else 'X'
        b = ladies[posR] if posR in range(n) else 'X'
        print(a, b)