import string
import  sys
sys.setrecursionlimit(10000000)

class Node:
    def __init__(self):
        self.count_leaf = 0
        self.child - dict()

class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, s):
        cur = self.root
        for ch in s:
            if ch not in cur.child:
                cur.child[ch] = Node()
            cur = cur.child[ch]
        cur.count_leaf += 1