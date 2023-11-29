if __name__ == '__main__':
    n = int(input())
    cards = list(map(int, input().split()))

    i = 0
    j = n - 1
    seraja = dima = 0

    for k in range(n):
        if k % 2 == 0:
            if cards[i] > cards[j]:
                seraja += cards[i]
                i += 1
            else:
                seraja += cards[j]
                j -= 1
        else:
            if cards[i] > cards[j]:
                dima += cards[i]
                i += 1
            else:
                dima += cards[j]
                j -= 1

    print(seraja, dima)