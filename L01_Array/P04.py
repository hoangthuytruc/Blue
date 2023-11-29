def increaseString(v) -> str:
    if len(v) == 1:
        return chr(ord(v) + 1)

    for index in range(len(v) - 1, -1, -1):
        if v[index] == 'z':
            v = v[:index] + 'a' + v[index + 1:]
            continue
        else:
            newChar = ord(v[index]) + 1
            v = v[:index] + chr(newChar) + v[index + 1:]
            break
    return v


def ascending(s1, s2) -> bool:
    if len(s2) == 1:
        return ord(s1) < ord(s2)

    for i in range(len(s1)):
        if ord(s1[i]) == ord(s2[i]):
            continue
        else:
            return ord(s1[i]) < ord(s2[i])
    return False


if __name__ == '__main__':
    s = input()
    t = input()

    newString = increaseString(s)
    if ascending(newString, t):
        print(newString)
    else:
        print("No such string")