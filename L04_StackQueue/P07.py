import queue

if __name__ == '__main__':
    n, b = map(int, input().split())
    q = queue.Queue()
    processing = 0
    for _ in range(n):
        t, d = map(int, input().split())
        while q.qsize() != 0 and t >= q.queue[0]:
            q.get()
        if q.qsize() <= b:
            processing = max(t, processing) + d
            q.put(processing)
            print(processing, end=' ')
        else:
            print(-1, end=' ')