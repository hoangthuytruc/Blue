import queue

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    pq = queue.PriorityQueue()
    for i in range(n):
        pq.put(-1 * numbers[i])
        if i < 2:
            print(-1)
        else:
            first = -1 * pq.get()
            second = -1 * pq.get()
            third = -1 * pq.get()
            print(first * second * third)
            pq.put(-first)
            pq.put(-second)
            pq.put(-third)
