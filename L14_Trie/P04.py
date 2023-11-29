class Node:
    def __init__(self):
        self.count = 0
        self.child = dict()


def addWord(root, s):
    tmp = root
    for ch in s:
        if not ch in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
        tmp.count += 1

def findWord(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return 0
        tmp = tmp.child[ch]
    return tmp.count

if __name__ == '__main__':
    n = int(input())
    root = Node()
    for _ in range(n):
        op = input().split()
        if op[0] == 'add':
            addWord(root, op[1])
        else:
            print(findWord(root, op[1]))