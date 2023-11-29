def checkJacket(n, v) -> bool:
    if n == 1:
        return v[0] == 1

    count = 0
    for index in range(n):
        if v[index] == 0:
            count += 1
            if count == 2:
                break

    if count == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    numberOfButtons = int(input())
    arrayOfButtons = list(map(int, input().split()))

    if checkJacket(numberOfButtons, arrayOfButtons):
        print("YES")
    else:
        print("NO")