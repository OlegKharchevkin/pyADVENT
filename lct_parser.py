from cmd_parser import cmd_parser
from arg_rename import arg_rename


def lct_parser(file: str, synonyms: dict):
    locations = {}
    with open(file, "r", encoding='utf-8') as f:
        number = 0
        buf = []
        mode = 0
        for i in f.readlines():
            if mode == 1:
                if i[0].isspace():
                    if len(i) < 4 or i[3].isspace():
                        locations[number][2][-1][1][-1].append(buf)
                        mode = 0
                        continue
                    buf.append(i[3:-1])
                elif i[0] == "*":
                    locations[number][2][-1][1][-1].append(buf)
                    mode = 0
                    continue
                else:
                    locations[number][2][-1][1][-1].append(buf)
                    mode = 0
            if mode == 0:
                if i[0].isspace() or i[0] == "*":
                    continue
                elif i[0] == "+":
                    number = int(i[3:-1])
                    locations[number] = ["", [], []]
                elif i[0] == "s":
                    locations[number][0] = i[3:-1]
                elif i[0] == "l":
                    if i[3] != ">":
                        locations[number][1].append(i[3:-1])
                elif i[0] == "t":
                    buf = cmd_parser(i)
                    arg_rename(buf, synonyms)
                    locations[number][2].append(buf)
                    if buf[1][-1][0] == '"':
                        buf = []
                        mode = 1
    return locations
