def popAll(st: list) -> str:
    operator_list = ""
    while len(st) != 0:
        c = st.pop()
        if c != "(":
            operator_list += c
        else:
            break
    return operator_list


def isOperator(c: str) -> bool:
    return not (c.isalpha() or c == "(" or c == ")")


if __name__ == '__main__':
    n = int(input())
    expressions = []
    reversed_exps = []

    for i in range(n):
        expressions.append(input())
        reversed_exps.append("")

    stack = []

    for i in range(n):
        s = expressions[i]
        for j in range(len(s)):
            if isOperator(s[j]) or s[j] == "(":
                stack.append(s[j])
            elif s[j] == ")":
                reversed_exps[i] += popAll(stack)
            elif s[j].isalpha():
                reversed_exps[i] += s[j]

    for element in reversed_exps:
        print(element)