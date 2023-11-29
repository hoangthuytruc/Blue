if __name__ == '__main__':
    lens = list(map(int, input().split()))
    elementNumbers = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    minCombination = a[0:elementNumbers[0]]
    b.reverse()
    maxCombination = b[0:elementNumbers[1]]

    if minCombination[len(minCombination) - 1] < maxCombination[len(maxCombination) - 1]:
        print("YES")
    else:
        print("NO")