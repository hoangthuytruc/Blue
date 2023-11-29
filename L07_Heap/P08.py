import queue


def solve():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b, d = map(int, input().split())
        jobs.append((d, a, b))

    jobs.sort()
    pq = queue.PriorityQueue()
    time = 0
    money = 0
    for d, a, b in jobs:
        time += b
        pq.put((-a, b, d))
        while time > d:
            ta, tb, td = pq.get()
            if tb > time - d:
                tb -= time - d
                money += (time - d) / -ta
                time = d
                pq.put((ta, tb, td))
            else:
                time -= tb
                money += tb / -ta
    print('{:.2f}'.format(money))


T = int(input())
for t in range(T):
    solve()