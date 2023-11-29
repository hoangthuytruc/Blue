import queue

if __name__ == '__main__':
    n = int(input())
    pq = queue.PriorityQueue()
    tmp = queue.PriorityQueue()
    for _ in range(n):
        t = list(map(int, input().split()))
        if t[0] == 1:
            pq.put(t[1])
        elif t[0] == 2:
            tmp.put(t[1])
        else:
            while not tmp.empty() and pq.queue[0] == tmp.queue[0]:
                pq.get()
                tmp.get()
            print(pq.queue[0])
