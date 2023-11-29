import heapq

if __name__ == '__main__':
    n = int(input())
    minHeap = []
    maxHeap = []
    nReviews = 0
    for _ in range(n):
        t = list(map(int, input().split()))

        if t[0] == 1:
            x = t[1]
            nReviews += 1

            if len(minHeap) != 0 and minHeap[0] < x:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
                heapq.heappush(minHeap, x)
            else:
                heapq.heappush(maxHeap, -x)

            if nReviews % 3 == 0:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        else:
            if len(minHeap) == 0:
                print("No reviews yet")
            else:
                print(minHeap[0])