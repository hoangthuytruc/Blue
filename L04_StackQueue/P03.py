import queue
if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            q = queue.Queue()
            discarded = []
            for i in range(1, n+1, +1):
                q.put(i)
            while q.qsize() > 1:
                discarded.append(q.get())
                q.put(q.get())
            if discarded:
                print("Discarded cards: " + ', '.join([str(elem) for elem in discarded]))
            else:
                print("Discarded cards:")
            print("Remaining card: " + str(q.get()))