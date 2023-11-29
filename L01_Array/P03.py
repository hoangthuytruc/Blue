if __name__ == '__main__':
    numberOfInterestingMinutes = int(input())
    arrayOfTime = list(map(int, input().split()))

    currentTime = 0
    for index in range(numberOfInterestingMinutes):
        if arrayOfTime[index] - currentTime > 15:
            currentTime += 15
            break
        else:
            currentTime = arrayOfTime[index]

    if currentTime == arrayOfTime[len(arrayOfTime) - 1]:
        extraTime = currentTime + 15
        if extraTime > 90:
            currentTime = 90
        else:
            currentTime = extraTime

    print(currentTime)