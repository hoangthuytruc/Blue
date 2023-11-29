if __name__ == '__main__':
    string = input()
    line = 1
    for i in range(len(string)):
        if ord(string[i]) < 97:
            line += 1
    print(line)