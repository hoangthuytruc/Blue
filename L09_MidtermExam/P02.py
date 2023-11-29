if __name__ == '__main__':
    n = int(input())
    if n < 26:
        print("NO")
    else:
        checked = [0] * 26
        string = list(input())
        for i in range(len(string)):
            index = abs(97 - ord(str(string[i]).lower()))
            checked[index] += 1
        isPangram = True
        for i in range(26):
            if checked[i] == 0:
                isPangram = False
                break
        print("YES" if isPangram else "NO")
