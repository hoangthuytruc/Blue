import queue


class Topic:
    def __init__(self, _id, _newScore, _change):
        self.id = _id
        self.newScore = _newScore
        self.change = _change

    def __lt__(self, other):
        if self.change == other.change:
            return self.id > other.id
        else:
            return self.change > other.change


if __name__ == '__main__':
    n = int(input())
    pq = queue.PriorityQueue()
    for _ in range(n):
        topicID, currentScore, post, like, comment, share = map(int, input().split())
        newScore = post * 50 + like * 5 + comment * 10 + share * 20
        pq.put(Topic(topicID, newScore, newScore - currentScore))
    for _ in range(5):
        top = pq.get()
        print(top.id, top.newScore)