if __name__ == '__main__':
    n = int(input())
    d = dict()
    d["Emperor Penguin"] = 0
    d["Macaroni Penguin"] = 0
    d["Little Penguin"] = 0
    for _ in range(n):
        penguin = input()
        d[penguin] += 1
    rs = max(d.values())
    for k in d.keys():
        if d[k] == rs:
            print(k)