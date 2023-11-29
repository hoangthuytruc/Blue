class Node:
    def __init__(self):
        self.weight = -1
        self.child = dict()


def addWord(root, s, w):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
        tmp.weight = max(tmp.weight, w)


def findWord(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return -1
        tmp = tmp.child[ch]
    return tmp.weight


if __name__ == '__main__':
    root = Node()
    n, q = map(int, input().split())
    for _ in range(n):
        s, w = input().split()
        addWord(root, s, int(w))
    for _ in range(q):
        s = input()
        print(findWord(root, s))