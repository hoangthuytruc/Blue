import heapq

if __name__ == '__main__':
    n = int(input())
    maxHeap = []
    minHeap = []
    taken = [False] * 1000001
    cost = 0
    billID = 0
    for _ in range(n):
        a = list(map(int, input().split()))
        for x in a[1:]:
            billID += 1
            heapq.heappush(maxHeap, (-x, billID))
            heapq.heappush(minHeap, (x, billID))

        while taken[maxHeap[0][1]]:
            heapq.heappop(maxHeap)

        while taken[minHeap[0][1]]:
            heapq.heappop(minHeap)
        taken[maxHeap[0][1]] = taken[minHeap[0][1]] = True
        cost += -heapq.heappop(maxHeap)[0] - heapq.heappop(minHeap)[0]
    print(cost)