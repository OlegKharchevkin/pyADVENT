def arg_rename(cmd_line: list, synonyms: dict):
    for index, i in enumerate(cmd_line[0]):
        if i[0] in ('o', 'a', 'h', 't', 'p', 'f'):
            if i[0] != '':
                cmd_line[0][index][1] = synonyms[i[1]]
    for index, i in enumerate(cmd_line[1]):
        if i[0] in ('d', '*', 'c', 'a', 'n'):
            if i[0] != '':
                cmd_line[1][index][1] = synonyms[i[1]]
