if __name__ == '__main__':
    chessboard = [[1, 4, 5, 16, 17],
               [2, 3, 6, 15, 18],
               [9, 8, 7, 14, 19],
               [10, 11, 12, 13, 20],
               [25, 24, 23, 22, 21]]
    board_dict = dict()
    for i in range(5):
        for j in range(5):
            board_dict[chessboard[i][j]] = (j+1, i+1)
    q = int(input())
    for i in range(q):
        time = int(input())
        if time % 25 == 0:
            x, y = board_dict[25]
        else:
            x, y = board_dict[time % 25]
        print("Case {}: {} {}".format(i+1, x, y))

