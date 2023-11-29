import queue

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        s = []
        q = queue.Queue()
        pq = queue.PriorityQueue()
        isStack = isQueue = isPQ = True

        for _ in range(n):
            a, b = map(int, input().split())
            if a == 1:
                s.append(b)
                q.put(b)
                pq.put(-b)
            else:
                if len(s) == 0:
                    isStack = isQueue = isPQ = False
                else:
                    if s.pop() != b:
                        isStack = False
                    if q.get() != b:
                        isQueue = False
                    if -pq.get() != b:
                        isPQ = False

        if not isStack and not isQueue and not isPQ:
            print("impossible")
        elif isStack + isQueue + isPQ > 1:
            print("not sure")
        elif isStack:
            print("stack")
        elif isQueue:
            print("queue")
        else:
            print("priority queue")