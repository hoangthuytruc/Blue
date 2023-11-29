if __name__ == '__main__':
    s = []
    mass = lambda  c : 1 if c == 'H' else 12 if c == 'C' else 16

    for c in input().strip():
        if c.isalpha():
            s.append(mass(c))
        elif c.isnumeric():
            top = s.pop()
            s.append(top * int(c))
        elif c == '(':
            s.append(-1)
        elif c == ')':
            total = 0
            while s[-1] != -1:
                total += s[-1]
                s.pop()
            s.pop()
            s.append(total)
    print(sum(s))