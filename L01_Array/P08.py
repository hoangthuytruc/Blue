if __name__ == '__main__':
    s = input()
    t = input()

    s_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict.keys():
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1

    t_dict = {}
    for i in range(len(t)):
        if t[i] in t_dict.keys():
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1

    for key in t_dict.keys():
        if not (key in s_dict.keys()):
            print("need tree")
            exit()

    array = automaton = False
    if len(t) < len(s):
        automaton = True

    match_index = -1
    for i in range(len(t)):
        index_in_s = s.find(t[i], match_index + 1)
        if index_in_s > match_index:
            match_index = index_in_s
        else:
            array = True
            break

    if array and automaton:
        print("both")
    elif array:
        print("array")
    else:
        print("automaton")