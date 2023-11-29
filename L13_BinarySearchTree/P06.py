class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.value:
        root.left = insert(root.left, x)
    elif x > root.value:
        root.right = insert(root.right, x)
    return root

def upperbound(root, x):
    if root is None:
        return root
    if root.value <= x:
        return upperbound(root.right, x)
    elif root.value > x:
        ub_left = upperbound(root.left, x)
        return root if ub_left is None else ub_left
n = input()
prices = list(map(int, input().split()))
min_loss = 10 ** 16
root = None

for sell_price in prices:
    best_buy_node = upperbound(root, sell_price)
    if best_buy_node is not None:
        min_loss = min(best_buy_node.value - sell_price, min_loss)
    root = insert(root, sell_price)
print(min_loss)