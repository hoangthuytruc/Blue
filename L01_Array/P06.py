def getBigSegment(s1, s2) -> list:
    return [min(s1[0], s2[0]), max(s1[1], s2[1])]


if __name__ == '__main__':
    segmentTotal = int(input())
    if segmentTotal == 1:
        print(1)
    else:
        bigSegment = list(map(int, input().split()))
        bigSegmentIndex = 0
        currentBigSegment = bigSegment

        for i in range(1, segmentTotal):
            i_segment = list(map(int, input().split()))
            currentBigSegment = getBigSegment(currentBigSegment, i_segment)
            if i_segment == currentBigSegment:
                bigSegment = currentBigSegment
                bigSegmentIndex = i

        if bigSegment == currentBigSegment:
            print(bigSegmentIndex + 1)
        else:
            print(-1)