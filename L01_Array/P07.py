def calBlockedTime(n, k) -> int:
    return (n // k) * 5


if __name__ == '__main__':
    passInfo = list(map(int, input().split()))
    passTotal = passInfo[0]
    failLimit = passInfo[1]

    bestTime = 0
    worstTime = 0
    passList = {}
    for i in range(passTotal):
        i_pass = input()
        key = str(len(i_pass))
        if key in passList.keys():
            passList[key] += 1
        else:
            passList[key] = 1

    rightPassLength = len(input())
    for key in passList.keys():
        if int(key) < rightPassLength:
            bestTime += passList[key]
    worstTime = bestTime + passList[str(rightPassLength)] - 1

    bestTime += calBlockedTime(bestTime, failLimit) + 1
    worstTime += calBlockedTime(worstTime, failLimit) + 1
    print(bestTime, worstTime)