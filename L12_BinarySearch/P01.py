import bisect
if __name__ == '__main__':
    count = 0
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break
        count += 1
        numbers = []
        for _ in range(n):
            numbers.append(int(input()))
        numbers.sort()
        print("CASE# {0}:".format(count))
        for i in range(k):
            c = int(input())
            idx = bisect.bisect_left(numbers, c, 0, n)
            if idx in range(0, n) and numbers[idx] == c:
                print("{0} found at {1}".format(c, idx + 1))
            else:
                print("{0} not found".format(c))