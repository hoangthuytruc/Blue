import queue

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        numbers = list(map(int, input().split()))
        pq = queue.PriorityQueue()
        for i in range(n):
            pq.put(numbers[i])
        cost = 0
        while len(pq.queue) > 1:
            first = pq.get()
            second = pq.get()
            pq.put(first + second)
            cost += first + second
        print(cost)