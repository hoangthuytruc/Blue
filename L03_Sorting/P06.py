if __name__ == '__main__':
    n = int(input())
    len_bars = list(map(int, input().split()))

    count = {}
    for element in len_bars:
        if element in count.keys():
            count[element] += 1
        else:
            count[element] = 1

    sorted_bars = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print(sorted_bars[0][1], len(sorted_bars))
