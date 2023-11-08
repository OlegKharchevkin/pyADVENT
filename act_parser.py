from cmd_parser import cmd_parser
from arg_rename import arg_rename


def act_parser(file: str,  synonyms: dict):
    actions = {}
    with open(file, "r", encoding='utf-8') as f:
        buf = []
        word = 0
        mode = 0
        for i in f.readlines():
            if mode == 1:
                if i[0].isspace():
                    if len(i) < 4 or i[3].isspace():
                        actions[word][-1][1][-1].append(buf)
                        mode = 0
                        continue
                    buf.append(i[3:-1])
                elif i[0] == "*":
                    actions[word][-1][1][-1].append(buf)
                    mode = 0
                    continue
                else:
                    actions[word][-1][1][-1].append(buf)
                    mode = 0
            if mode == 0:
                if i[0].isspace() or i[0] == "*":
                    continue
                elif i[0] == "+":
                    buf = [j[:4] for j in i[3:-1].split()]
                    word = buf[0]
                    for j in buf:
                        synonyms[j] = word
                    actions[word] = []
                elif i[0] == "a":
                    buf = cmd_parser(i)
                    arg_rename(buf, synonyms)
                    actions[word].append(buf)
                    if len(buf[1]) > 0 and buf[1][-1][0] == '"':
                        buf = []
                        mode = 1
    return actions
