import bisect

if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        fr, price = map(int, input().split())
        moneys = list(map(int, input().split()))
        moneys.sort()
        checked = [False for _ in range(fr)]

        count = 0
        for i in range(fr):
            if not checked[i]:
                pos = bisect.bisect_left(moneys, price - moneys[i])
                if pos in range(0, fr) and pos != i and not checked[pos] and moneys[pos] == price - moneys[i]:
                    checked[pos] = True
                    checked[i] = True
                    count += 1
        print(count)