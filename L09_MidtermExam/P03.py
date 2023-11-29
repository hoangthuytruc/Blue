if __name__ == '__main__':
    k, n, w = map(int, input().split())
    money = 0
    total = 0
    for i in range(1, w+1):
        total += i * k
        if total > n:
            money = total - n
    print(money)