message = input()
newspaper = input()
a = dict([(i, 0) for i in range(52)])
b = dict([(i, 0) for i in range(52)])

for c in message:
    id = ord(c) - 65
    if c > 'Z':
        id = ord(c) - 97 + 26
    if not id in a:
        a[id] = 1
    else:
        a[id] += 1

for c in newspaper:
    id = ord(c) - 65
    if c > 'Z':
        id = ord(c) - 97 + 26
    if not id in b:
        b[id] = 1
    else:
        b[id] += 1
yay = 0
whoops = 0
for i in range(52):
    tmp = min(a[i], b[i])
    yay += tmp
    a[i] -= tmp
    b[i] -= tmp

for i in range(26):
    whoops += min(a[i], b[i + 26]) + min([a[i + 26], b[i]])
print("%d %d" % (yay, whoops))